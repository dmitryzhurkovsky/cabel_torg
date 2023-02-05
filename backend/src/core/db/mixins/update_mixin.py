from fastapi import HTTPException
from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin, TableType, UpdateBaseSchema


class UpdateMixin(BaseMixin):
    @classmethod
    async def update(
            cls, session: AsyncSession,
            pk: int,
            input_data: UpdateBaseSchema | dict
    ) -> TableType | HTTPException:
        """Update object by primary keys"""
        await session.execute(
            update(cls.table).
            where(cls.table.id == pk).
            values(**(input_data if isinstance(input_data, dict) else input_data.__dict__))
        )
        await session.commit()

        result = await session.execute(
            select(cls.table).
            options(*cls.preloaded_fields).
            where(cls.table.id == pk)
        )

        return result.scalars().first()

    @classmethod
    async def update_m2m(cls, session: AsyncSession, input_data: UpdateBaseSchema | dict) -> TableType | HTTPException:
        """Update m2m object"""
        filter_fields = cls.init_m2m_filtered_fields(
            filter_fields=input_data if isinstance(input_data, dict) else input_data.__dict__
        )
        await session.execute(
            update(cls.table).
            values(**(input_data if isinstance(input_data, dict) else input_data.__dict__)).
            where(*filter_fields)
        )
        await session.commit()

        result = await session.execute(
            select(cls.table).
            where(*filter_fields)
        )

        return result.scalars().first()
