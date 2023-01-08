import re
from xml.etree.ElementTree import Element

import bcrypt
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import QueryParams

from src.core.managers.category_manager import CategoryManager
from src.models import Category
from src.models.product_models import Product


async def convert_filter_fields(filter_fields: QueryParams, session: AsyncSession = None) -> list:
    """Convert filter values to SQLALCHEMY filter expressions"""
    converted_filter_fields = []

    if price_gte := filter_fields.get('price_gte'):
        converted_filter_fields.append(Product.price >= int(price_gte))

    if price_lte := filter_fields.get('price_lte'):
        converted_filter_fields.append(Product.price <= int(price_lte))

    if category_id := filter_fields.get('category_id'):
        categories_ids = await CategoryManager.get_categories_ids(
            session=session, parent_category_ids=[int(category_id)]
        )
        converted_filter_fields.append(Product.category_id.in_(categories_ids))

    if search_letters := filter_fields.get('q'):
        category_ids_query = await session.execute(
            select(Category.id).
            filter(Category.name.ilike(f'%{search_letters}'))
        )
        category_ids = category_ids_query.scalars().all()

        converted_filter_fields.append(or_(
            Product.name.ilike(f'%{search_letters}%'),
            Product.vendor_code.ilike(f'%{search_letters}%'),
            Product.description.ilike(f'%{search_letters}%'),
            Product.category_id.in_(category_ids),
        ))

    return converted_filter_fields


def password_is_valid(password: str, password_hash: str) -> bool:
    """Check whether a password is valid."""
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def hash_password(password: str) -> str:
    """Hash a password by bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def clean_fields(fields: dict) -> dict:
    """Delete None elements from dict"""
    prepared_fields = dict()
    for key, value in fields.items():
        if value:
            prepared_fields[key] = value

    return prepared_fields


def clean_string_from_spaces_and_redundant_symbols(dirty_string: str) -> str | None:
    """Clean an input element from any redundant symbols and spaces."""
    if len(dirty_string) == 1 and dirty_string == '.':
        return None
    return re.findall(pattern='[А-Яа-яЁёa-zA-Z0-9].+[А-Яа-яЁёa-zA-Z.0-9)"]', string=dirty_string)[0]


def get_tag_name(raw_field: Element) -> str:
    return raw_field.tag.split('}')[-1]
