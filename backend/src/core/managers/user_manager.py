from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import TableType, CreateBaseSchema
from src.core.managers.base_manager import CRUDManager
from src.core.utils import hash_password
from src.models.user_model import User
from src.rest.schemas.user_schema import UserCreateSchema, UserUpdateSchema


class UserManager(CRUDManager):

    table = User
    create_scheme = UserCreateSchema
    update_scheme = UserUpdateSchema

    @classmethod
    def create(
            cls,
            input_data: CreateBaseSchema,
            session: AsyncSession,
    ) -> TableType:
        input_data.password = hash_password(password=input_data.password)
        return super().create(input_data, session)
