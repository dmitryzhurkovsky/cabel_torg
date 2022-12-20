from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.exception.base_exception import BadRequestError, ObjectNotFoundError
from src.core.managers.user_manager import UserManager
from src.rest.schemas.user_schema import UserSchema, UserCreateSchema, UserUpdateSchema
from src.services.auth_service import AuthService

user_router = APIRouter(tags=['users'])


@user_router.get('/users/<user_id>', response_model=UserSchema)
async def get_user(
        user_id: int, session: AsyncSession = Depends(get_session)
) -> UserSchema:
    user = await UserManager.retrieve(id=user_id, session=session)
    return user


@user_router.get('/users/mine', response_model=UserSchema)
async def get_current_user(
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> UserSchema:
    user = await UserManager.retrieve(id=user.id, session=session)
    return user


@user_router.post('/users/', response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
        user: UserCreateSchema, session: AsyncSession = Depends(get_session)
) -> UserSchema:
    try:
        user_db = await UserManager.retrieve(email=user.email, session=session)

        if user_db:
            raise BadRequestError(detail='User with such email exists')

    except ObjectNotFoundError:
        user = await UserManager.create(input_data=user, session=session)

        return user


@user_router.patch('/users/mine', response_model=UserSchema)
async def update_info_about_current_user(
        user_info: UserUpdateSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    user = await UserManager.update(
        session=session,
        pk=user.id,
        input_data=user_info,
        partial=True
    )
    return user
