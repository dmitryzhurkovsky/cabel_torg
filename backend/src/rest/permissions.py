from starlette.authentication import AuthenticationBackend
from starlette.requests import Request

from src.core import settings
from src.core.db.db import async_session
from src.core.exception.base_exception import ForbiddenError, InvalidTokenError
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


def is_authenticated_permissions(request: Request):
    if not request.user:
        raise InvalidTokenError


def is_admin_permissions(request: Request):
    is_authenticated_permissions(request=request)

    if not request.user.is_admin:
        raise ForbiddenError


def is_owner_permissions(request: Request):
    is_authenticated_permissions(request=request)
    if not request.user.is_admin:
        raise ForbiddenError


def is_admin_or_owner_permissions(request: Request):
    return is_owner_permissions(request=request) or is_admin_permissions(request=request)
