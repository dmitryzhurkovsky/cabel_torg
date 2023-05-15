from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def values(cls) -> tuple:
        return tuple(el.value for el in cls)


class SessionStatusEnum(str, Enum):
    """
    It's used in queries to a database.
    """
    SUCCESS = 'Success'
    FAILURE = 'Failure'


class ProductTypeFilterEnum(str, Enum):
    """
    It's query params for Product.
    """
    WITH_DISCOUNT = 'with_discount'
    AVAILABLE = 'available'
    POPULAR = 'popular'


class CategoryTypeFilterEnum(str, Enum):
    """
    It's query params for Category.
    """
    WITH_DISCOUNT = 'with_discount'
    QUICK = 'quick'


class ProductOrderFilterEnum(str, Enum):
    """
    It's query params for ordering of Product.
    """
    CREATED_DATE_ASCENDING = 'created_at'
    CREATED_DATE_DESCENDING = '-created_at'
    PRICE_ASCENDING = 'actual_price'
    PRICE_DESCENDING = '-actual_price'
    DISCOUNT_ASCENDING = 'discount'
    DISCOUNT_DESCENDING = '-discount'
