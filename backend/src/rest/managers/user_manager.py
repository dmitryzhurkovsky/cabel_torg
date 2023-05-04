from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import TableType
from src.core.utils import hash_password, generate_random_password
from src.models.user_model import User
from src.rest.managers.base_manager import CRUDManager
from src.rest.schemas.user_schema import UserCreateSchema, UserUpdateSchema


class UserManager(CRUDManager):
    table = User
    create_scheme = UserCreateSchema
    update_scheme = UserUpdateSchema

    @classmethod
    async def create(
            cls,
            input_data: UserCreateSchema | dict,
            session: AsyncSession,
    ) -> TableType:
        input_data.password = hash_password(password=input_data.password)  # make it better
        return await super().create(input_data, session)

    @classmethod
    async def update(
            cls, session: AsyncSession,
            pk: int,
            input_data: UserUpdateSchema | dict
    ) -> TableType | HTTPException:
        if new_password := input_data.get('password'):  # todo make it better
            input_data['password'] = hash_password(password=new_password)
        return await super().update(session, pk, input_data)
