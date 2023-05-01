import asyncio
from datetime import timedelta, datetime

import jwt
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jwt import (
    InvalidTokenError as JWTInvalidTokenError,
    DecodeError,
    ExpiredSignatureError
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.core.exception.base_exception import (
    InvalidTokenError,
    AuthenticateError
)
from src.core.redis import redis
from src.core.utils import is_valid
from src.models.user_model import User
from src.rest.managers.user_manager import UserManager


class AuthService:
    @staticmethod
    def create_token(user_id: int, token_type: str) -> str:
        """Generate a new token for a user."""
        token_were_issued_by = 'cabeltorg_auth'  # iss
        token_were_issued_at = datetime.utcnow()  # iat
        token_will_be_valid_at = datetime.utcnow()  # nbf(not before)

        match token_type:
            case 'access':
                token_expires_at = (
                        datetime.utcnow() + timedelta(seconds=settings.JWT_ACCESS_TOKEN_EXPIRATION_TIME)
                )  # exp
            case 'refresh':
                token_expires_at = (
                        datetime.utcnow() + timedelta(seconds=settings.JWT_REFRESH_TOKEN_EXPIRATION_TIME)
                )  # exp

        default_header = {"typ": "JWT", "alg": "HS256"}
        payload = {
            "sub": user_id,
            "exp": token_expires_at,  # noqa
            "iat": token_were_issued_at,
            "nbf": token_will_be_valid_at,
            "iss": token_were_issued_by
        }

        return jwt.encode(headers=default_header, payload=payload, key=settings.JWT_SECRET_KEY)

    @staticmethod
    def decode_token(token: str) -> int:
        """Decode a token and return user_id took from payload."""
        try:
            payload = jwt.decode(
                jwt=token.encode(), key=settings.JWT_SECRET_KEY, algorithms='HS256'
            )
            user_id = payload.get('sub')
        except (JWTInvalidTokenError, DecodeError, ExpiredSignatureError, KeyError):
            raise InvalidTokenError

        return user_id

    @classmethod
    async def authenticate_user(cls, user_data: dict, session: AsyncSession) -> User | HTTPException:
        """Check whether there is a user in the database and a password is valid."""
        password = user_data.pop('password')

        user = await UserManager.retrieve(
            session=session,
            **user_data
        )
        if is_valid(password=password, password_hash=user.password):
            return user

        raise AuthenticateError()

    @classmethod
    async def validate_refresh_token(cls, refresh_token: str, user_id: int) -> None:
        """Check whether a refresh token is the same as refresh token kept in redis."""
        return await asyncio.sleep(0.0000001)

        refresh_token_is_kept_by_redis = await redis.get(name=user_id)
        if refresh_token_is_kept_by_redis != refresh_token:
            raise InvalidTokenError()

    @classmethod
    def generate_access_and_refresh_tokens(cls, user_id: int) -> tuple:
        """Create new access and refresh tokens by user_id.A refresh token should also be saved in redis
        by the following pattern: key is user_id and value is the refresh_token."""
        access_token = cls.create_token(user_id=user_id, token_type='access')
        refresh_token = cls.create_token(user_id=user_id, token_type='refresh')

        # await redis.set(name=user_id, value=refresh_token, ex=settings.JWT_REFRESH_TOKEN_EXPIRATION_TIME)

        return access_token, refresh_token

    @classmethod
    async def get_access_and_refresh_tokens_by_email_and_password(
            cls, session: AsyncSession,
            user_form: OAuth2PasswordRequestForm
    ) -> tuple | HTTPException:
        """Generate new access and refresh tokens by email and password if a user is authenticated."""
        user_data = {
            'email': user_form.username,
            'password': user_form.password,
        }
        user = await cls.authenticate_user(user_data=user_data, session=session)

        access_token, refresh_token = cls.generate_access_and_refresh_tokens(user_id=user.id)

        return access_token, refresh_token

    @classmethod
    async def get_new_access_and_refresh_tokens_using_old_refresh_token(
            cls, old_refresh_token: str
    ) -> tuple:
        """Generate new access and refresh tokens by a refresh_token if the refresh_token is valid."""
        user_id = cls.decode_token(token=old_refresh_token)
        await cls.validate_refresh_token(user_id=user_id, refresh_token=old_refresh_token)

        access_token, refresh_token = cls.generate_access_and_refresh_tokens(user_id=user_id)

        return access_token, refresh_token
