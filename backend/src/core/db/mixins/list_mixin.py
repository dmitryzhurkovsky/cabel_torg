from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            prefetch_fields: tuple = None,
            filter_fields: dict = {},
            offset: int = 0,
            limit: int = 100
    ) -> list:
        """Get list of objects"""
        options = cls.init_prefetch_related_fields(prefetch_fields=prefetch_fields)

        objects = await session.execute(
            select(cls.table).
            filter_by(**filter_fields).
            options(*options).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all()
