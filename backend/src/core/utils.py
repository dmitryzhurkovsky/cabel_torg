import secrets
import string
from decimal import Decimal

import bcrypt

from src.models.product_model import Product


def generate_random_password() -> str:
    """Generate a random password. It's used for generating the password when an user create
    an order without creating the user."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(20))


def is_valid(password: str, password_hash: str) -> bool:
    """Check whether a password is valid."""
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def hash_password(password: str) -> str:
    """Hash a password by bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def calculate_price_with_discount(product: Product, discount: int) -> Decimal:
    """Calculate a price based on a discount"""
    return Decimal(product.price - (product.price * discount / 100))
