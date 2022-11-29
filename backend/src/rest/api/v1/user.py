from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.exception.base_exception import BadRequestError, ObjectNotFoundError
from src.core.managers.user_manager import UserManager
from src.rest.schemas.user_schema import UserInDBBaseSchema, UserCreateSchema

user_router = APIRouter(tags=['users'])


@user_router.get('/users/<user_id>', response_model=UserInDBBaseSchema)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await UserManager.retrieve(id=user_id, session=session)
    return user


@user_router.post('/users/', response_model=UserInDBBaseSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreateSchema, session: AsyncSession = Depends(get_session)):
    try:
        user_db = await UserManager.retrieve(email=user.email, session=session)

        if user_db:
            raise BadRequestError(detail='User with such email exists')

    except ObjectNotFoundError:
        user = await UserManager.create(input_data=user, session=session)

        return user
