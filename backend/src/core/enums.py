from enum import Enum


class TypeOfProduct(str, Enum):
    """
    It's query params for Product
    """
    ALL = 'all'
    WITH_DISCOUNT = 'with_discount'
    AVAILABLE = 'available'
