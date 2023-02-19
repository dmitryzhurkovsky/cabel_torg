from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            filter_by: dict = {},  # noqa
            where: tuple | list = (),
            order_by: tuple | list = (),
            offset: int = 0,
            limit: int = 100,
    ) -> list:
        """Get list of objects"""
        objects = await session.execute(
            select(cls.table).
            filter_by(**filter_by).
            where(*where).
            options(*cls.preloaded_fields).
            order_by(*order_by).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all()
