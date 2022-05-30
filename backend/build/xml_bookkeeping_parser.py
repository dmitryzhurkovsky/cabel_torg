# from src.settings import settings
from xml.etree import ElementTree

from _elementtree import Element
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import database_services

from src.models.product_models import Category, Manufacturer, Product

import inspect


class XMLParser:
    __slots__ = ('file', 'namespaces', 'root', 'db')

    def __init__(self, db: AsyncSession):
        # self.xml_file = settings.XML_BOOKKEEPING_FILE_PATH
        self.file = 'build/test_1.xml'
        self.namespaces = {'urn': 'urn:1C.ru:commerceml_2'}
        self.root = ElementTree.parse(self.file).getroot()
        self.db = db

    @property
    def is_execute_parsing_of_categories(self) -> bool:
        return 'categories' == inspect.stack()[-13].function.split('_')[-1]

    @property
    def is_execute_parsing_of_goods(self) -> bool:
        return 'parse_goods' in [el.function for el in inspect.stack()]

    @staticmethod
    def category_has_subcategories(category: Element) -> bool:
        return len(category) > 2

    async def clean_field(self, raw_field: Element) -> tuple[str, str|int] | tuple[None, None]:
        match raw_field.tag.split('}')[-1]:
            case 'Ид':
                return 'bookkeeping_id', raw_field.text
            case 'Наименование':
                return 'name', raw_field.text
            case 'Артикул':
                return 'vendor_code', raw_field.text
            case 'БазоваяЕдиница':
                return 'base_unit', raw_field[0][0].text.strip()
            case 'Группы':
                if self.is_execute_parsing_of_goods:
                    category = await database_services.get(
                        db=self.db, model=Category, fields={'bookkeeping_id': raw_field[0].text}
                    )

                    if category:
                        return 'category_id', category.id

                    print(f'Skipped record {raw_field[0].text}')
                return None, None
            case 'Описание':
                return 'description', raw_field.text
            case 'Картинка':
                return 'image_path', raw_field.text  # todo path to picture
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

    async def clean_element(self, element: Element) -> dict:
        clean_element = {}

        for raw_field in element:
            field_name, value = await self.clean_field(raw_field=raw_field)
            if field_name and value:
                clean_element[field_name] = value

        return clean_element

    async def parse_and_write_category_and_subcategories_to_database(
            self,
            raw_categories: Element,
            parent_category_id: int = None,
    ):
        for raw_category in raw_categories:
            clean_category = await self.clean_element(element=raw_category)

            if parent_category_id:
                clean_category |= {'parent_category_id': parent_category_id}

            db_category, _ = await database_services.get_or_create(db=self.db, model=Category, fields=clean_category)

            if self.category_has_subcategories(category=raw_category):
                await self.db.refresh(db_category)

                subcategories = raw_category[2]
                await self.parse_and_write_category_and_subcategories_to_database(
                    raw_categories=subcategories, parent_category_id=int(db_category.id)
                )

    async def parse_categories(self):
        main_categories = self.root[0][3]
        await self.parse_and_write_category_and_subcategories_to_database(raw_categories=main_categories)

    async def parse_goods(self):
        goods = self.root[1][4]

        for product in goods:
            clean_product = await self.clean_element(element=product)
            db_product, _ = await database_services.get_or_create(db=self.db, model=Product, fields=clean_product)
