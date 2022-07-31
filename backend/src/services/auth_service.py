from datetime import timedelta, datetime

import jwt
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.redis import redis
from src.core import settings
from src.core.exception.base_exception import InvalidTokenError, AuthenticateError
from src.core.managers.user_manager import UserManager
from src.core.utils import check_password
from src.models.user_model import User
from src.rest.schemas.auth_schema import (
    AuthenticationResponseSchema,
    RefreshTokenBaseSchema,
)


class AuthService:
    @staticmethod
    async def create_token(user_id: int, token_type: str) -> str:
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

        token = jwt.encode(headers=default_header, payload=payload, key=settings.JWT_SECRET_KEY)

        if token_type == 'refresh':
            await redis.set(name=user_id, value=token, ex=settings.JWT_REFRESH_TOKEN_EXPIRATION_TIME)

        return token

    @classmethod
    async def authenticate_user(cls, user_data: dict, session: AsyncSession) -> User | HTTPException:
        password = user_data.pop('password')

        user = await UserManager.retrieve(
            session=session,
            **user_data
        )
        if check_password(password_hash=user.password, password=password):
            return user

        raise AuthenticateError()

    @classmethod
    async def generate_access_and_refresh_token(
            cls, session: AsyncSession,
            user_form: OAuth2PasswordRequestForm
    ) -> AuthenticationResponseSchema | HTTPException:
        user_data = {
            'username': user_form.username,
            'password': user_form.password,
        }
        user = await cls.authenticate_user(user_data=user_data, session=session)

        return AuthenticationResponseSchema(
            access_token=await cls.create_token(user_id=user.id, token_type='access'),
            refresh_token=await cls.create_token(user_id=user.id, token_type='refresh')
        )

    @classmethod
    async def validate_refresh_token(cls, refresh_token: str, user_id: int):
        refresh_token_is_kept_by_redis = await redis.get(name=user_id)
        if refresh_token_is_kept_by_redis != refresh_token:
            raise InvalidTokenError()

    @classmethod
    async def generate_new_refresh_token(cls, old_refresh_token: str) -> RefreshTokenBaseSchema:
        payload = jwt.decode(
            jwt=old_refresh_token.encode(), key=settings.JWT_SECRET_KEY, algorithms='HS256'
        )
        user_id = payload.get('sub')

        await cls.validate_refresh_token(user_id=user_id, refresh_token=old_refresh_token)

        new_refresh_token = await cls.create_token(user_id=user_id, token_type='refresh')

        return RefreshTokenBaseSchema(refresh_token=new_refresh_token)
