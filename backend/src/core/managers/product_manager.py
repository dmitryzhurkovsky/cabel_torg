from fastapi import Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.retrieve_mixin import RetrieveMixin
from src.core.utils import convert_filter_fields
from src.models.product_models import Product


class ProductManager(ListMixin, RetrieveMixin, DeleteMixin):
    table = Product

    @classmethod
    async def filter_list(
            cls,
            request: Request,
            session: AsyncSession,
            prefetch_fields: tuple = None,
            offset: int = 0,
            limit: int = 12
    ) -> list:
        """Get list of objects"""
        options = cls.init_prefetch_related_fields(prefetch_fields=prefetch_fields)
        filter_fields = convert_filter_fields(filtered_fields=request.query_params)

        objects = await session.execute(
            select(cls.table).
            filter(*filter_fields).
            options(*options).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all()
