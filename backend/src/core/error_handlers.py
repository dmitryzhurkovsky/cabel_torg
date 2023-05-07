import re

from fastapi import Request, status
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse

from src.app import app
from src.core.exception.base_exception import (
    AuthenticateError,
    InvalidTokenError,
    BadRequestError,
    ObjectNotFoundError,
    ForbiddenError
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


@app.exception_handler(ForbiddenError)
async def forbidden_error_handler(request: Request, exception: AuthenticateError) -> JSONResponse:
    """Handle an forbidden error"""
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


@app.exception_handler(IntegrityError)
async def integrity_error(request: Request, exception: IntegrityError) -> JSONResponse:
    """Handle a bad request error"""
    foreign_keys_indvalid = re.findall(r'(\w+_id)', exception.args[0])
    if foreign_keys_indvalid:
        detail = f'The following fields are invalid: {foreign_keys_indvalid}'
    else:
        detail = exception.args[0]

    return JSONResponse(
        status_code=BadRequestError.status_code,
        content={'detail': detail}
    )
