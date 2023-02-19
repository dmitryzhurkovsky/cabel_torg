from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.sql.functions import count
from starlette.datastructures import QueryParams

from src.managers.base_manager import CRUDManager
from src.core.utils import (
    get_filter_expressions,
    calculate_price_with_discount,
    get_order_expressions
)
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
        search_fields = await get_filter_expressions(filter_fields, session=session)
        search_fields.append(Product.is_visible.is_not(False))

        order_by = get_order_expressions(filter_fields)

        return await cls.list(
            session=session,
            where=search_fields,
            order_by=order_by,
            offset=offset,
            limit=limit
        )

    @classmethod
    async def get_count_of_products(
            cls,
            filter_fields: QueryParams,
            session: AsyncSession,
    ) -> int:
        filter_fields = await get_filter_expressions(filter_fields, session=session)
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
        price_with_discount = calculate_price_with_discount(product=product, discount=input_data.discount)

        # we do one extra query here, but since we do it rarely it's ok for us.
        await cls.update(pk=pk, session=session, input_data={
            'price_with_discount': price_with_discount,
            'discount': input_data.discount
        })
        return product

    @classmethod
    async def bulk_update_discounts(
            cls, session: AsyncSession,
            categories_ids: tuple,
            discount: int
    ):
        products = await cls.list(session=session, where=(
            Product.category_id.in_(categories_ids),
            Product.personal_discount == 0
        ))
        for product in products:
            product.price_with_discount = calculate_price_with_discount(product=product, discount=discount)
        # we don't do commit here because we should also update a category
