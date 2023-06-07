from fastapi import HTTPException
from sqlalchemy import ColumnOperators
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import QueryParams

from src.core.db.mixins.base_mixin import TableType
from src.core.enums import UserTypeFilterEnum
from src.core.utils import hash_password
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

    @staticmethod
    def get_filter_expressions(filter_fields: QueryParams) -> list[ColumnOperators]:
        filter_expressions = []

        if type_of_category := filter_fields.get('type_of_user'):
            if type_of_category == UserTypeFilterEnum.ADMIN:
                filter_expressions.append(User.is_admin.is_(True))

        return filter_expressions

    @classmethod
    async def filter_list(
            cls,
            filters: QueryParams,
            session: AsyncSession,
            custom_preloaded_fields: tuple | list = (),
            offset: int = 0,
            limit: int = 100
    ) -> list:
        """Get filtered list of objects with pagination."""
        filter_expressions = cls.get_filter_expressions(filters)

        return await cls.list(
            session=session,
            where=filter_expressions,
            custom_preloaded_fields=custom_preloaded_fields,
            offset=offset,
            limit=limit
        )
