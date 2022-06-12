from enum import Enum


class SessionStatusEnum(str, Enum):
    """
    It's used in queries to a database.
    """
    SUCCESS = 'Success'
    FAILURE = 'Failure'


class TypeOfProduct(str, Enum):
    """
    It's query params for Product
    """
    ALL = 'all'
    WITH_DISCOUNT = 'with_discount'
    AVAILABLE = 'available'
