from fastapi import APIRouter, Depends, status
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from src.core.db.db import get_session
from src.core.enums import SessionStatusEnum
from src.core.exception.base_exception import BadRequestError, ObjectNotFoundError, ForbiddenError
from src.core.utils import generate_random_password
from src.rest.managers.user_manager import UserManager
from src.rest.permissions import is_admin_permission, is_authenticated_permission
from src.rest.schemas.user_schema import (
    UserSchema,
    UserCreateSchema,
    UserUpdateSchema,
    UserInputCreateSchema,
    RecoveryPasswordSchema
)
from src.services.user_service import UserService

user_router = APIRouter(tags=['users'], prefix='/users')


@user_router.get('/check_email/<email>')
async def get_users(
        email: EmailStr | None = None,
        session: AsyncSession = Depends(get_session)
) -> dict:
    try:
        await UserManager.retrieve(email=email, session=session)
    except ObjectNotFoundError:
        return {'message': 'False'}

    return {'message': 'True'}


@user_router.get(
    '/<user_id>',
    response_model=UserSchema,
    dependencies=[Depends(is_admin_permission)]
)
async def get_user(
        user_id: int,
        session: AsyncSession = Depends(get_session)
) -> UserSchema:
    return await UserManager.retrieve(id=user_id, session=session)


@user_router.get(
    '/mine',
    response_model=UserSchema,
    dependencies=[Depends(is_authenticated_permission)]
)
async def get_current_user(
        request: Request,
        session: AsyncSession = Depends(get_session)
) -> UserSchema:
    return await UserManager.retrieve(id=request.user.id, session=session)


@user_router.post(
    '',
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
        user_info: UserInputCreateSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
) -> UserSchema:
    if (
            user_info.is_admin and
            not request.user or
            not request.user.is_admin
    ):
        raise ForbiddenError('Only a user with admin role can create new admin users.')

    try:
        user_db = await UserManager.retrieve(email=user_info.email, session=session)
        if user_db:
            raise BadRequestError(detail='User with such email exists')
    except ObjectNotFoundError:
        user_info = user_info.dict()
        password_is_generated = user_info.pop('isGenerated', None)
        user_db = await UserManager.create(input_data=UserCreateSchema(**user_info), session=session)
        generated_password = user_info.get('password') if password_is_generated else None
        UserService.send_confirmation_url(user=user_db, generated_password=generated_password)

        return user_db


@user_router.patch(
    '/mine',
    response_model=UserSchema,
    dependencies=[Depends(is_authenticated_permission)]
)
async def update_info_about_current_user(
        user_info: UserUpdateSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
):
    return await UserManager.update(
        session=session, pk=request.user.id, input_data=user_info.dict(exclude_unset=True)
    )


@user_router.post(
    '/reset_password',
    status_code=status.HTTP_201_CREATED,
)
async def reset_user_password(
        user_info: RecoveryPasswordSchema,
        session: AsyncSession = Depends(get_session)
):
    user = await UserManager.retrieve(email=user_info.email, session=session)

    new_password = generate_random_password()
    await UserManager.update(pk=user.id, session=session, input_data={'password': new_password})
    UserService.send_new_password(user=user, new_password=new_password)

    return {'status': SessionStatusEnum.SUCCESS.value}
