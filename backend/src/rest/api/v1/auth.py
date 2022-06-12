from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.schemas.auth_schema import AuthenticationResponseSchema, RefreshTokenBaseSchema
from src.services.auth_service import AuthService

from fastapi import status

auth_router = APIRouter(tags=['auth'])


@auth_router.post('/token', response_model=AuthenticationResponseSchema, status_code=status.HTTP_201_CREATED)
async def get_access_and_refresh_token(
        user_data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_session)
):
    auth_credentials = await AuthService.generate_access_and_refresh_token(session=session, user_data=user_data)
    return auth_credentials


@auth_router.post('/refresh', response_model=RefreshTokenBaseSchema, status_code=status.HTTP_201_CREATED)
async def generate_new_refresh_token(
        refresh_token: RefreshTokenBaseSchema,
):
    refresh_token = await AuthService.generate_new_refresh_token(old_refresh_token=refresh_token.refresh_token)
    return refresh_token
