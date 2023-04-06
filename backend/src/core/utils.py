from decimal import Decimal

import bcrypt

from src.models.product_model import Product


def is_valid(password: str, password_hash: str) -> bool:
    """Check whether a password is valid."""
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def hash_password(password: str) -> str:
    """Hash a password by bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def calculate_price_with_discount(product: Product, discount: int) -> Decimal:
    """Calculate a price based on a discount"""
    return Decimal(product.price - (product.price * discount / 100))
