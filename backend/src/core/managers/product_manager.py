from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import QueryParams

from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.retrieve_mixin import RetrieveMixin
from src.core.utils import convert_filter_fields
from src.models import Product


class ProductManager(
    ListMixin,
    RetrieveMixin,
    DeleteMixin
):
    table = Product

    @classmethod
    async def filter_list(
            cls,
            filter_fields: QueryParams,
            session: AsyncSession,
            prefetch_fields: tuple = None,
            offset: int = 0,
            limit: int = 12
    ) -> list:
        """Get filtered list of objects with pagination."""
        options = cls.init_prefetch_related_fields(prefetch_fields=prefetch_fields)
        filter_fields = await convert_filter_fields(filter_fields, session=session)

        objects = await session.execute(
            select(cls.table).
            filter(*filter_fields).
            options(*options).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all()
