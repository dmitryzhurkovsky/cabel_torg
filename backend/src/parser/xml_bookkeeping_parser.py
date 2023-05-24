from abc import ABC

from src.core import settings
from src.parser.mixins.category_mixin import CategoryMixin
from src.parser.mixins.good_mixin import GoodsMixin
from src.parser.mixins.offer_mixin import OfferMixin


class XMLParser(CategoryMixin, GoodsMixin, ABC):
    """The parser that take a xml file with 1C dump and maps data to a database."""
    XML_FILE = settings.BOOKKEEPING_FILE_PATH

    __slots__ = ('db',)


class OffersParser(OfferMixin, ABC):
    """The parser that take a xml file with 1C dump of prices and maps data to a database."""
    XML_FILE = settings.FILE_WITH_PRICES_PATH

    __slots__ = ('db',)
