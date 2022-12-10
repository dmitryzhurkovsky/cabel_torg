from src.core import settings
from xml.etree import ElementTree

from _elementtree import Element
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import database_services
from src.core.utils import prepare_fields, clean_string_from_spaces_and_redundant_symbols
from src.models import BaseUnit

from src.models.product_models import Product
from src.models.category_model import Category
from src.models.manufacturer_model import Manufacturer

import inspect


class XMLParser:
    """The parser that take a xml file with 1C dump and maps data to a database."""
    __slots__ = ('file', 'namespaces', 'root', 'db')

    def __init__(self, db: AsyncSession):
        self.file = settings.XML_BOOKKEEPING_FILE_PATH
        self.namespaces = {'urn': 'urn:1C.ru:commerceml_2'}
        self.root = ElementTree.parse(self.file).getroot()
        self.db = db

    @property
    def is_executing_parsing_of_goods(self) -> bool:
        """Check whether we are parsing goods now."""
        return 'parse_goods' in [el.function for el in inspect.stack()]

    @staticmethod
    def category_has_subcategories(category: Element) -> bool:
        """Check whether an input category has subcategories."""
        return len(category) > 2

    async def clean_field(self, raw_field: Element) -> tuple[str, str | int] | tuple[None, None]:
        """Transform an element of a xml tree to "ready to write to a database" state."""
        field_name, field_value = None, None

        match raw_field.tag.split('}')[-1]:
            # todo Make it by dict
            case 'Ид':
                return 'bookkeeping_id', raw_field.text
            case 'Наименование':
                field_name, field_value = 'name', raw_field.text
            case 'Артикул':
                field_name, field_value = 'vendor_code', raw_field.text
            case 'БазоваяЕдиница':
                code = raw_field.attrib.get('Код')
                full_name = raw_field.attrib.get('НаименованиеПолное')
                international_abbreviated = raw_field.attrib.get('МеждународноеСокращение')
                prepared_fields = prepare_fields(
                    {
                        'code': code,
                        'full_name': full_name,
                        'international_abbreviated': international_abbreviated
                    }
                )
                base_unit, _ = await database_services.get_or_create(
                    db=self.db, model=BaseUnit, fields=prepared_fields
                )
                await self.db.refresh(base_unit)

                if base_unit:
                    return 'base_unit_id', base_unit.id
            case 'Группы':
                if self.is_executing_parsing_of_goods:
                    category = await database_services.get(
                        db=self.db, model=Category, fields={'bookkeeping_id': raw_field[0].text}
                    )

                    if category:
                        return 'category_id', category.id

                    print(f'Skipped record {raw_field[0].text}')
                return None, None  # It means it's been checking a main node of category nodes
            case 'Описание':
                field_name, field_value = 'description', raw_field.text
            case 'Картинка':
                field_name, field_value = 'image_path', raw_field.text
            case 'Изготовитель':
                manufacturer, _ = await database_services.get_or_create(
                    db=self.db, model=Manufacturer, fields={
                        'bookkeeping_id': raw_field[0].text,
                        'name': raw_field[1].text
                    }
                )
                await self.db.refresh(manufacturer)
                return 'manufacturer_id', manufacturer.id
            case 'СтавкиНалогов':
                if raw_field[0][1].text == 'Без НДС':
                    return None, None
                return 'tax', int(raw_field[0][1].text)
            case _:
                return None, None

        if field_name and field_value:
            return field_name, clean_string_from_spaces_and_redundant_symbols(field_value)

        return None, None

    async def clean_element(self, element: Element) -> dict:
        """
        Clean an input elements group or an input element of a xml tree
        and transform its fields to "ready to write to a database" state.
        """
        clean_element = {}

        for raw_field in element:
            field_name, field_value = await self.clean_field(raw_field=raw_field)
            if field_name and field_value:
                clean_element[field_name] = field_value

        return clean_element

    @staticmethod
    def get_subcategories(category: Element) -> Element:
        """Return subcategories of an input category."""
        return category[2]

    async def parse_category_and_subcategories(
            self,
            raw_categories: Element,
            parent_category_id: int = None,
    ):
        """Parse category's elements and write them to database."""
        for raw_category in raw_categories:
            clean_category = await self.clean_element(element=raw_category)

            if parent_category_id:
                clean_category |= {'parent_category_id': parent_category_id}

            db_category, _ = await database_services.get_or_create(db=self.db, model=Category, fields=clean_category)

            if self.category_has_subcategories(category=raw_category):
                await self.db.refresh(db_category)

                subcategories = self.get_subcategories(category=raw_category)
                await self.parse_category_and_subcategories(
                    raw_categories=subcategories, parent_category_id=int(db_category.id)
                )

    async def parse_categories(self):
        """Parse "Категории" node and write then to a database."""
        main_categories = self.root[0][3]
        await self.parse_category_and_subcategories(raw_categories=main_categories)

    async def parse_goods(self):
        """Parse "Товары" node  and write then to a database."""
        goods = self.root[1][4]

        for product in goods:
            clean_product = await self.clean_element(element=product)
            await database_services.get_or_create(db=self.db, model=Product, fields=clean_product)
