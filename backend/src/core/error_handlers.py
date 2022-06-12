from fastapi import Request, status
from pydantic import ValidationError
from starlette.responses import JSONResponse

from src.app import app
from src.core.exception.base_exception import (
    AuthenticateError,
    InvalidTokenError,
    BadRequestError,
    ObjectNotFoundError
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exception: ValidationError) -> JSONResponse:
    """Handle an invalid data error"""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'detail': 'Provided values are not valid.', 'metadata': f'{exception}'}
    )


@app.exception_handler(AuthenticateError)
async def unauthorized_error_handler(request: Request, exception: AuthenticateError) -> JSONResponse:
    """Handle an unauthorized error"""
    return JSONResponse(
        status_code=exception.status_code, content={'detail': exception.detail}, headers=exception.headers
    )


@app.exception_handler(InvalidTokenError)
async def invalid_token_error_handler(request: Request, exception: InvalidTokenError) -> JSONResponse:
    """Handle an invalid access or refresh token error"""
    return JSONResponse(status_code=exception.status_code, content={'detail': exception.detail})


@app.exception_handler(BadRequestError)
async def bad_request_error_handler(request: Request, exception: BadRequestError) -> JSONResponse:
    """Handle a bad request error"""
    return JSONResponse(status_code=exception.status_code, content={'detail': exception.detail})


@app.exception_handler(ObjectNotFoundError)
async def object_not_found_error_handler(request: Request, exception: ObjectNotFoundError) -> JSONResponse:
    """Handle a bad request error"""
    return JSONResponse(status_code=exception.status_code, content={'detail': exception.detail})
