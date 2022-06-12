from fastapi import HTTPException
from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin, TableType
from src.rest.schemas.base_schema import BaseSchema


class UpdateMixin(BaseMixin):
    @classmethod
    async def update(cls, session: AsyncSession, input_data: BaseSchema) -> TableType | HTTPException:
        """Update object by primary keys"""
        await session.execute(
            update(cls.table).
            filter(cls.table.id == input_data.id).
            values(**input_data.__dict__)
        )
        await session.commit()

        result = await session.execute(
            select(cls.table).
            filter(cls.table.id == input_data.id)
        )

        return result.scalars().first()
