from decimal import Decimal

import bcrypt
from sqlalchemy import or_, select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import ColumnOperators
from starlette.datastructures import QueryParams

from src.core.enums import ProductOrderFilterEnum, ProductTypeFilterEnum
from src.models import Category
from src.models.product_models import Product, ProductStatus


async def get_filter_expressions(filter_fields: QueryParams, session: AsyncSession) -> list:
    """Convert filter values to SQLALCHEMY filter expressions."""
    from src.core.managers.category_manager import CategoryManager

    filter_expressions = []

    price_gte = filter_fields.get('price_gte')
    if price_gte:
        filter_expressions.append(Product.price >= Decimal(price_gte))
    else:
        filter_expressions.append(Product.price > Decimal(0))

    if price_lte := filter_fields.get('price_lte'):
        filter_expressions.append(Product.price <= Decimal(price_lte))

    if category_id := filter_fields.get('category_id'):
        categories_ids = await CategoryManager.get_categories_ids(
            session=session, parent_category_ids=[int(category_id)]
        )
        filter_expressions.append(Product.category_id.in_(categories_ids))

    if type_of_product := filter_fields.get('type_of_product'):
        if type_of_product == ProductTypeFilterEnum.AVAILABLE:
            filter_expressions.append(Product.status == ProductStatus.AVAILABLE.value)
        elif type_of_product == ProductTypeFilterEnum.WITH_DISCOUNT:
            filter_expressions.append(and_(
                Product.discount.is_not(None),
                Product.discount != 0,
            ))

    if search_letters := filter_fields.get('q'):
        category_ids_query = await session.execute(
            select(Category.id).
            where(Category.name.ilike(f'%{search_letters}'))
        )
        category_ids = category_ids_query.scalars().all()

        filter_expressions.append(or_(
            Product.name.ilike(f'%{search_letters}%'),
            Product.vendor_code.ilike(f'%{search_letters}%'),
            Product.description.ilike(f'%{search_letters}%'),
            Product.category_id.in_(category_ids),
        ))

    return filter_expressions


def get_order_expressions(filter_fields: QueryParams) -> list[ColumnOperators | None]:
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


async def delivery_type_is_valid(pk: int, session: AsyncSession) -> list:
    D


def password_is_valid(password: str, password_hash: str) -> bool:
    """Check whether a password is valid."""
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def hash_password(password: str) -> str:
    """Hash a password by bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def calculate_price_with_discount(product: Product, discount: int) -> Decimal:
    return Decimal(product.price - (product.price * discount / 100))
