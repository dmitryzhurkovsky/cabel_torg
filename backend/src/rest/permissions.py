from starlette.requests import Request

from src.core.exception.base_exception import ForbiddenError, InvalidTokenError


def is_authenticated_permission(request: Request):
    if not request.user:
        raise InvalidTokenError


def is_admin_permission(request: Request):
    is_authenticated_permission(request=request)

    if not request.user.is_admin:
        raise ForbiddenError


def is_owner_permission(request: Request):
    is_authenticated_permission(request=request)
    if not request.user.is_admin:
        raise ForbiddenError


def is_admin_or_owner_permission(request: Request):
    return is_owner_permission(request=request) or is_admin_permission(request=request)
