from _elementtree import Element
from xml.etree import ElementTree

from sqlalchemy.ext.asyncio import AsyncSession

from src.parser.utils import clean_string_from_spaces_and_redundant_symbols


class BaseMixin:
    """A base mixin that implements functionality are required in all mixins."""
    NAMESPACES = {'urn': 'urn:1C.ru:commerceml_2'}
    CACHE = dict()  # todo use a cache library here

    __slots__ = ('db', 'parsed_categories_ids')

    def __init__(self, db: AsyncSession):
        self.db = db
        self.parsed_categories_ids = set()
        self.CACHE['attributes'] = dict()
        self.CACHE['attributes']['under_the_order'] = set()
        self.CACHE['values'] = dict()
        self.CACHE['names'] = dict()

    @property
    def root_element(cls):  # noqa
        if getattr(cls, 'XML_FILE'):
            return ElementTree.parse(cls.XML_FILE).getroot()  # noqa
        raise AttributeError('The XML_FILE variable should be declared.')

    @staticmethod
    def clean_common_field(raw_field: Element) -> tuple[str, str] | tuple[None, None]:
        """Parse an element of a xml tree and transform fields are common for all instances or at least 2."""
        match raw_field.tag.split('}')[-1]:
            # todo Make it by dict
            case 'Ид':
                return 'bookkeeping_id', raw_field.text
            case 'Наименование':
                return 'name', clean_string_from_spaces_and_redundant_symbols(raw_field.text)
            case _:
                return None, None

    async def parse_instance(self):
        """Parse `instance` node and then write them to a database."""
        raise NotImplementedError

    async def clean_element(self, element: Element) -> dict:
        """
        Clean an input elements group or an input element of a xml tree
        and transform its fields to "ready to write to a database" state.
        """
        raise NotImplementedError

    async def clean_fields(self, raw_field: Element) -> tuple[str, str] | tuple[None, None]:
        """A method that clean fields required models. Should be implemented for each parser independently."""
        raise NotImplementedError
