from typing import TypeVar

from src.core.db.db import Base

TableType = TypeVar('TableType', bound=Base)


class BaseMixin:
    """Base async database mixin"""

    table: TableType
