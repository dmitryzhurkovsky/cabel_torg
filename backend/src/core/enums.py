from enum import Enum


class SessionStatusEnum(str, Enum):
    """
    It's used in queries to a database.
    """
    SUCCESS = 'Success'
    FAILURE = 'Failure'


class ProductTypeFilter(str, Enum):
    """
    It's query params for Product
    """
    ALL = 'all'
    WITH_DISCOUNT = 'with_discount'
    AVAILABLE = 'available'


class ProductType(str, Enum):
    """
    It's query params for Product
    """
    WITH_DISCOUNT = 'with_discount'
    AVAILABLE = 'available'

    @classmethod
    def values(cls) -> tuple:
        return tuple(el.value for el in cls)

