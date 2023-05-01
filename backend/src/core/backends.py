from starlette.authentication import AuthenticationBackend
from starlette.requests import Request

from src.core import settings
from src.core.db.db import async_session
from src.core.exception.base_exception import InvalidTokenError
from src.rest.managers.user_manager import UserManager
from src.services.auth_service import AuthService


class BearerTokenAuthBackend(AuthenticationBackend):
    """
    This is a custom auth backend class that will allow you to authenticate
    your request and return auth and user as a tuple.
    """

    async def authenticate(self, request: Request):
        user = None

        if payload := request.headers.get('Authorization', None):
            token_type, access_token = payload.split()
            if token_type != settings.JWT_TYPE:
                return

            try:
                user_id = AuthService.decode_token(token=access_token)
                async with async_session() as session:
                    user = await UserManager.retrieve(session=session, id=user_id)
            except InvalidTokenError:
                pass

        return settings.JWT_TYPE, user
