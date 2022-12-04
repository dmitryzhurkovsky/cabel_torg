import bcrypt
from starlette.datastructures import QueryParams

from src.core.enums import TypeOfProduct
from src.models.product_models import Product


def convert_filter_fields(filtered_fields: QueryParams) -> list:
    """Convert filter values to SQLALCHEMY filter expressions"""
    converted_filter_fields = []

    type_of_product = filtered_fields.get('type_of_product')
    if type_of_product != TypeOfProduct.ALL.value:
        converted_filter_fields.append(Product.type_of_products == type_of_product)

    price_gte = filtered_fields.get('price_gte')
    if price_gte:
        converted_filter_fields.append(Product.price >= int(price_gte))

    price_lte = filtered_fields.get('price_lte')
    if price_gte:
        converted_filter_fields.append(Product.price <= int(price_lte))

    category_id = filtered_fields.get('category_id')
    if category_id:
        converted_filter_fields.append(Product.category_id == int(category_id))

    search_letters = filtered_fields.get('q')
    if search_letters:
        converted_filter_fields.append(Product.name.like('%'+search_letters+'%'))

    return converted_filter_fields


def password_is_valid(password: str, password_hash: str) -> bool:
    """Check whether a password is valid."""
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def hash_password(password: str) -> str:
    """Hash a password by bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
