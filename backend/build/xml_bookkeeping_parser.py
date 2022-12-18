from mixins.category_mixin import CategoryMixin
from mixins.goods_mixin import GoodsMixin


class XMLParser(CategoryMixin, GoodsMixin):
    """The parser that take a xml file with 1C dump and maps data to a database."""
