from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            prefetch_fields: tuple = None,
            selected_fields: tuple = (),
            filter_fields: dict = {},  # noqa
            search_fields: tuple = (),
            order_fields: tuple = (),
            offset: int = 0,
            limit: int = 100,
    ) -> list:
        """Get list of objects"""
        options = cls.init_prefetch_related_fields(prefetch_fields=prefetch_fields)
        selected_columns = cls.init_selected_fields(selected_fields=selected_fields)

        objects = await session.execute(
            select(*selected_columns).
            filter_by(**filter_fields).
            filter(*search_fields).
            options(*options).
            order_by(*order_fields).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all() if not selected_fields else objects.all()
