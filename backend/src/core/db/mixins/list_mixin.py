from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.core.db.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            prefetch_fields: tuple = None,
            offset: int = 0,
            limit: int = 100
    ) -> list:
        """Get list of objects"""
        options = [selectinload(field) for field in prefetch_fields] if prefetch_fields else []

        objects = await session.execute(
            select(cls.table).
            options(*options).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all()
