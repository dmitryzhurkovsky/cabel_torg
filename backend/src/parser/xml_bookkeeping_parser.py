from abc import ABC

from src.parser.mixins.category_mixin import CategoryMixin
from src.parser.mixins.goods_mixin import GoodsMixin


class XMLParser(CategoryMixin, GoodsMixin, ABC):
    """The parser that take a xml file with 1C dump and maps data to a database."""
    __slots__ = ('db',)
