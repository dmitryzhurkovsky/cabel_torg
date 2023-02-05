from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.sql.functions import count
from starlette.datastructures import QueryParams

from src.core.managers.base_manager import CRUDManager
from src.core.utils import convert_filter_fields, calculate_price_with_discount
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
        search_fields = await convert_filter_fields(filter_fields, session=session)
        search_fields.append(Product.is_visible.is_not(False))
        return await cls.list(search_fields=search_fields, offset=offset, limit=limit, session=session)

    @classmethod
    async def get_count_of_products(
            cls,
            filter_fields: QueryParams,
            session: AsyncSession,
    ) -> int:
        filter_fields = await convert_filter_fields(filter_fields, session=session)
        filter_fields.append(Product.is_visible.is_not(False))

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
        product = await cls.retrieve(id=pk, session=session)
        product.price_with_discount = calculate_price_with_discount(product=product, discount=input_data.discount)
        await session.commit()
        return product

    @classmethod
    async def bulk_update_discounts(
            cls, session: AsyncSession,
            categories_ids: tuple,
            discount: int
    ):
        products = await cls.list(
            session=session,
            search_fields=(
                Product.category_id.in_(categories_ids),
                Product.discount == 0
            )
        )
        for product in products:
            product.price_with_discount = calculate_price_with_discount(product=product, discount=discount)
        # we don't do commit here because we should also update a category
