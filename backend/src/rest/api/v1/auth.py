from fastapi import APIRouter, Depends, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.schemas.auth_schema import AuthenticationResponseSchema
from src.services.auth_service import AuthService

from fastapi import status, Response

auth_router = APIRouter(tags=['auth'])


@auth_router.post('/token', response_model=AuthenticationResponseSchema, status_code=status.HTTP_201_CREATED)
async def obtain_pair_of_tokens_by_email_and_password(
        response: Response,
        user_form: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_session),
) -> AuthenticationResponseSchema:
    access_token, refresh_token = await AuthService.get_access_and_refresh_tokens_by_email_and_password(
        session=session, user_form=user_form
    )
    response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)

    return AuthenticationResponseSchema(access_token=access_token)


@auth_router.post('/refresh', status_code=status.HTTP_201_CREATED)
async def obtain_pair_of_tokens_by_refresh_token(refresh_token: str = Cookie(None)):
    await AuthService.get_new_access_and_refresh_tokens_using_old_refresh_token(
        old_refresh_token=refresh_token)
