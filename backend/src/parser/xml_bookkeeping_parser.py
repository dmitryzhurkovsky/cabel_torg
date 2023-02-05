from abc import ABC

from src.core import settings
from src.parser.mixins.category_mixin import CategoryMixin
from src.parser.mixins.goods_mixin import GoodsMixin
from src.parser.mixins.price_mixin import PriceMixin


class XMLParser(CategoryMixin, GoodsMixin, ABC):
    """The parser that take a xml file with 1C dump and maps data to a database."""
    XML_FILE = settings.XML_BOOKKEEPING_FILE_PATH

    __slots__ = ('db',)


class PricesParser(PriceMixin, ABC):
    """The parser that take a xml file with 1C dump of prices and maps data to a database."""
    XML_FILE = settings.PATH_TO_XML_FILE_WITH_PRICES

    __slots__ = ('db',)
    # todo add excluded categories
