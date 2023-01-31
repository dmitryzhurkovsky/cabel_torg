from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            filter_fields: dict = {},  # noqa
            search_fields: tuple | list = (),
            order_fields: tuple | list = (),
            offset: int = 0,
            limit: int = 100,
    ) -> list:
        """Get list of objects"""
        objects = await session.execute(
            select(cls.table).
            filter_by(**filter_fields).
            where(*search_fields).
            options(*cls.preloaded_fields).
            order_by(*order_fields).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all()
