from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy import or_, select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.sql.functions import count, func
from sqlalchemy.sql.operators import ColumnOperators
from starlette.datastructures import QueryParams

from src.core import settings
from src.core.enums import ProductOrderFilterEnum, ProductTypeFilterEnum
from src.core.utils import calculate_price_with_discount
from src.models import Product, Category, ProductOrder
from src.models.product_model import ProductStatus
from src.rest.managers.base_manager import CRUDManager
from src.rest.schemas.product_schema import ProductUpdateSchema


class ProductManager(CRUDManager):
    table = Product

    preloaded_fields = (
        joinedload(Product.manufacturer),
        joinedload(Product.category),
        selectinload(Product.attributes)  # todo change it and use joinedload instead of this one
    )

    @classmethod
    async def get_filter_expressions(cls, filter_fields: QueryParams, session: AsyncSession) -> list[ColumnOperators]:
        """Convert filter values to SQLALCHEMY filter expressions."""
        from src.rest.managers.category_manager import CategoryManager

        filter_expressions = []

        price_gte = filter_fields.get('actual_price_gte')
        if price_gte and price_gte != '0':
            filter_expressions.append(
                Product.actual_price >= Decimal(float(price_gte) / (1 + settings.DEFAULT_TAX / 100))
            )
        else:
            filter_expressions.append(Product.price > Decimal(0))

        if price_lte := filter_fields.get('actual_price_lte'):
            filter_expressions.append(
                Product.actual_price <= Decimal(float(price_lte) / (1 + settings.DEFAULT_TAX / 100))
            )

        if category_id := filter_fields.get('category_id'):
            categories_ids = await CategoryManager.get_categories_ids(
                session=session, parent_category_ids=[int(category_id)]
            )
            filter_expressions.append(Product.category_id.in_(categories_ids))

        if type_of_product := filter_fields.get('type_of_product'):
            if type_of_product in (
                    ProductTypeFilterEnum.WITH_DISCOUNT,
                    ProductTypeFilterEnum.NEW,
                    ProductTypeFilterEnum.AVAILABLE
            ):
                filter_expressions.append(Product.status == ProductStatus.AVAILABLE.value)

            if type_of_product == ProductTypeFilterEnum.WITH_DISCOUNT:
                filter_expressions.append(and_(
                    Product.price_with_discount.is_not(None),
                    Product.price > Product.price_with_discount,  # noqa
                ))
            elif type_of_product == ProductTypeFilterEnum.POPULAR:
                popular_products_ids = await cls.get_the_most_popular_products_ids(session=session)
                filter_expressions.append(Product.id.in_(popular_products_ids))
            elif type_of_product == ProductTypeFilterEnum.NEW:
                filter_expressions.append(Product.is_new.is_(True))

        if search_letters := filter_fields.get('q'):
            category_ids_query = await session.execute(
                select(Category.id).
                where(
                    Category.name.ilike(f'%{search_letters}')
                )
            )
            category_ids = category_ids_query.scalars().all()

            filter_expressions.append(or_(
                Product.name.ilike(f'%{search_letters}%'),
                Product.vendor_code.ilike(f'%{search_letters}%'),
                Product.description.ilike(f'%{search_letters}%'),
                Product.category_id.in_(category_ids),
            ))

        return filter_expressions

    @classmethod
    def get_order_expressions(cls, filter_fields: QueryParams) -> list[ColumnOperators | None]:
        """Convert ordering values to SQLALCHEMY filter expressions."""
        order_expressions = []
        if order_attribute := filter_fields.get('ordering'):
            if order_attribute in (
                    ProductOrderFilterEnum.CREATED_DATE_ASCENDING,
                    ProductOrderFilterEnum.PRICE_ASCENDING,
                    ProductOrderFilterEnum.DISCOUNT_ASCENDING
            ):
                order_expressions.append(getattr(Product, order_attribute).asc())
            elif order_attribute in (
                    ProductOrderFilterEnum.CREATED_DATE_DESCENDING,
                    ProductOrderFilterEnum.PRICE_DESCENDING,
                    ProductOrderFilterEnum.DISCOUNT_DESCENDING
            ):
                order_expressions.append(getattr(Product, order_attribute[1:]).desc())

        return order_expressions

    @classmethod
    async def filter_list(
            cls,
            filters: QueryParams,
            session: AsyncSession,
            offset: int = 0,
            limit: int = 12
    ) -> list:
        """Get filtered list of objects with pagination."""
        filter_expressions = await cls.get_filter_expressions(filters, session=session)
        filter_expressions.append(Product.is_visible.is_not(False))

        order_by = cls.get_order_expressions(filters)

        return await cls.list(
            session=session,
            where=filter_expressions,
            order_by=order_by,
            offset=offset,
            limit=limit
        )

    @classmethod
    async def get_the_most_popular_products_ids(cls, session: AsyncSession) -> list[int]:
        result = await session.execute(
            select(Product.id).
            join(Product.added_to_orders).
            group_by(Product.id).
            order_by(func.count(ProductOrder.product_id).desc()).
            limit(20)
        )

        return result.scalars().all()  # noqa

    @classmethod
    async def get_count_of_products(
            cls,
            filters: QueryParams,
            session: AsyncSession,
    ) -> int:
        filter_expressions = await cls.get_filter_expressions(filters, session=session)
        filter_expressions.append(Product.is_visible.is_not(False))

        result = await session.execute(
            select(count()).
            select_from(
                select(cls.table.id).
                where(*filter_expressions).
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
            categories_ids: tuple[int] | list[int],
            discount: int
    ):
        products = await cls.list(
            session=session,
            where=(
                Product.category_id.in_(categories_ids),
                Product.discount == 0,
            ),
            limit=1000000
        )
        for product in products:
            product.price_with_discount = calculate_price_with_discount(product=product, discount=discount)
        # we don't do commit here because we should also update a category
