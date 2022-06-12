from fastapi import status


class BaseError(Exception):
    status_code: int
    default_detail: str
    default_headers: dict | None = None

    def __init__(self, detail: str = None, headers: dict = None):
        self.detail = detail or self.default_detail
        self.headers = headers or self.default_headers


class AuthenticateError(BaseError):
    """
    Authentication verifies who the user is.
    Authentication works through passwords, one-time pins, biometric information,
     and other information provided or entered by the user.
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Invalid username or password'
    default_headers = ({'WWW-Authenticate': 'Bearer'},)


class InvalidTokenError(AuthenticateError):
    default_detail = 'This token have already been used or is invalid'


class ForbiddenError(BaseError):
    """
    Authorization determines what resources a user can access.
    Authorization always takes place after authentication.
    """
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Forbidden'


class BadRequestError(BaseError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid data'


class ObjectNotFoundError(BaseError):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Not found'
