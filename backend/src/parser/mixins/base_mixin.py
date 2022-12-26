from _elementtree import Element

from src.core.utils import clean_string_from_spaces_and_redundant_symbols
from src.core import settings
from xml.etree import ElementTree

from sqlalchemy.ext.asyncio import AsyncSession


class BaseMixin:
    """A base mixin that implements functionality are required in all mixins."""
    XML_FILE = settings.XML_BOOKKEEPING_FILE_PATH
    NAMESPACES = {'urn': 'urn:1C.ru:commerceml_2'}
    ROOT_ELEMENT = ElementTree.parse(XML_FILE).getroot()
    CACHE = dict()  # todo use a cache library here

    __slots__ = ('db',)

    def __init__(self, db: AsyncSession):
        self.db = db

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
