from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.sql.functions import count
from starlette.datastructures import QueryParams

from src.core.managers.base_manager import CRUDManager
from src.core.utils import convert_filter_fields
from src.models import Product
from src.rest.schemas.product_schema import ProductUpdateSchema


class ProductManager(CRUDManager):
    table = Product
    preloaded_fields = (
        joinedload(Product.manufacturer),
        joinedload(Product.category),
        selectinload(Product.attributes)  # todo change it and use joinedload instead of this one
    )

    @classmethod
    async def filter_list(
            cls,
            filter_fields: QueryParams,
            session: AsyncSession,
            offset: int = 0,
            limit: int = 12
    ) -> list:
        """Get filtered list of objects with pagination."""
        filter_fields = await convert_filter_fields(filter_fields, session=session)

        objects = await session.execute(
            select(cls.table).
            where(*filter_fields).
            options(*cls.preloaded_fields).
            limit(limit).
            offset(offset)
        )

        return objects.scalars().all()

    @classmethod
    async def get_count_of_products(
            cls,
            filter_fields: QueryParams,
            session: AsyncSession,
    ) -> int:
        filter_fields = await convert_filter_fields(filter_fields, session=session)

        result = await session.execute(
            select(count()).
            select_from(
                select(cls.table.id).
                where(*filter_fields).
                subquery()
            )
        )
        return result.scalar()

    @classmethod
    async def update_discount(
            cls, session: AsyncSession,
            pk: int,
            input_data: ProductUpdateSchema
    ) -> Product | HTTPException:
        """Update object by primary keys"""
        query_result = await session.execute(
            select(cls.table).
            options(*cls.preloaded_fields).
            where(cls.table.id == pk)
        )
        product = query_result.scalars().first()

        product.price_with_discount = product.price - (product.price * input_data.discount / 100)

        await session.commit()
        return product
