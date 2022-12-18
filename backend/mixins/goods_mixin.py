from _elementtree import Element

from mixins.base_mixin import BaseMixin
from src.core.db import database_services
from src.core.utils import clean_string_from_spaces_and_redundant_symbols, clean_fields, get_tag_name
from src.models import Manufacturer, BaseUnit, Category

from src.models.product_models import Product

import inspect


class GoodsMixin(BaseMixin):
    @property
    def is_executing_parsing_of_goods(self) -> bool:  # todo delete?
        """Check whether we are parsing goods now."""
        return 'parse_goods' in [el.function for el in inspect.stack()]

    async def parse_products(self):
        """Parse "Товары" node and then write them to a database."""
        goods = self.ROOT_ELEMENT[1][4]  # noqa

        for product in goods:
            clean_product = await self.clean_product(element=product)
            await database_services.get_or_create(db=self.db, model=Product, fields=clean_product)  # noqa

    async def clean_product(self, element: Element) -> dict:
        """
        Clean a product(it's Товар in a xml tree) and transform its fields
        to "ready to write to a database" state.
        """
        clean_element = {}
        images = []

        for raw_field in element:
            field_name, field_value = await self.clean_product_field(raw_field=raw_field)
            if field_name and field_value:

                if field_name == 'image_path':
                    images.append(field_value)
                else:
                    clean_element[field_name] = field_value

        clean_element['images'] = ",".join(image for image in images)

        return clean_element

    async def clean_product_field(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Convert raw fields that are called by Russian language to an English alternative and
        if it's required make a query to a database to get id of a nested model.
        """
        field_name, field_value = self.clean_common_field(raw_field=raw_field)

        if field_name and field_value:
            return field_name, field_value

        match get_tag_name(raw_field):
            case 'БазоваяЕдиница':
                return await self.clean_product_base_unit(raw_field=raw_field)
            case 'Изготовитель':
                return await self.clean_product_manufacturer(raw_field=raw_field)
            case 'Группы':
                return await self.clean_product_category(raw_field=raw_field)
            case 'ЗначениеСвойства':
                return self.clean_product_attributes(raw_field=raw_field)
            case 'СтавкиНалогов':
                if raw_field[0][1].text == 'Без НДС':
                    return None, None
                return 'tax', int(raw_field[0][1].text)
            case 'Артикул':
                field_name, field_value = 'vendor_code', raw_field.text
            case 'Описание':
                field_name, field_value = 'description', raw_field.text
            case 'Картинка':
                field_name, field_value = 'image_path', raw_field.text
            case _:
                return None, None

        if field_name and field_value:
            return field_name, clean_string_from_spaces_and_redundant_symbols(field_value)

    async def clean_product_base_unit(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean a product(it's БазоваяЕдиница in a xml tree) and
        transform its fields to "ready to write to a database" state.
        """
        code = raw_field.attrib.get('Код')
        full_name = raw_field.attrib.get('НаименованиеПолное')
        international_abbreviated = raw_field.attrib.get('МеждународноеСокращение')

        fields = clean_fields({
            'code': code,
            'full_name': full_name,
            'international_abbreviated': international_abbreviated
        })

        base_unit, _ = await database_services.get_or_create(
            db=self.db, model=BaseUnit, fields=fields  # noqa
        )
        await self.db.refresh(base_unit)  # noqa

        if base_unit:
            return 'base_unit_id', base_unit.id

    async def clean_product_manufacturer(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean a manufacturer(it's Производитель in a xml tree) and
        transform its fields to "ready to write to a database" state.
        """
        manufacturer, _ = await database_services.get_or_create(
            db=self.db, model=Manufacturer, fields={  # noqa
                'bookkeeping_id': raw_field[0].text,
                'name': raw_field[1].text
            })
        await self.db.refresh(manufacturer)  # noqa

        return 'manufacturer_id', manufacturer.id

    async def clean_product_category(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean a category(it's Группы in a xml tree) and transform its fields to "ready to write to a database" state.
        """
        category = await database_services.get(
            db=self.db, model=Category, fields={'bookkeeping_id': raw_field[0].text}  # noqa
        )

        if category:
            return 'category_id', category.id

        print(f'Skipped record {raw_field[0].text}')  # todo add logger

    def clean_product_attributes(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean an attributes(it's ЗначенияСвойств in a xml tree) and
        transform its fields to "ready to write to a database" state.
        """
        raise NotImplementedError

    async def parse_attributes(self):
        """Parse "Свойства" node and then write theirs fields to memory."""
        attributes = self.ROOT_ELEMENT[0][4]  # noqa
        attributes_cache = self.CACHE['attributes'] = dict()  # initiate aт attributes cache

        for attribute in attributes:
            clean_attribute = await self.clean_attribute(element=attribute)

            attribute_id = clean_attribute.pop('bookkeeping_id')
            attributes_cache[attribute_id] = clean_attribute  # noqa
            # todo use a cache(redis for example) here

    async def clean_attribute(self, element: Element) -> dict:
        """
        Clean an attribute(it's Свойство in a xml tree) and
        transform its fields to "ready to write to a database" state.
        """
        clean_element = {}

        for raw_field in element:
            field_name, field_value = self.clean_attribute_field(raw_field=raw_field)

            if field_name and field_value:
                clean_element[field_name] = field_value

        return clean_element

    def clean_attribute_field(self, raw_field: Element) -> tuple[str, int | list[dict]] | tuple[None, None]:
        """
        Clean attribute's fields(It's fields of Свойство).
        """
        if get_tag_name(raw_field) == 'ВариантыЗначений':
            return 'value_options', self.clean_attribute_value_options(raw_field=raw_field)

        field_name, field_value = self.clean_common_field(raw_field=raw_field)

        return field_name, field_value

    def clean_attribute_value_options(self, raw_field: Element) -> list[dict]:
        """Clean value options(It's fields of ВариантыЗначений)."""
        available_value_options = []
        for value in raw_field:
            value_option = {}
            for value_option_field in value:
                field_name, field_value = self.clean_attribute_value_options_field(value_option_field)
                if field_name and field_value:
                    value_option[field_name] = field_value

            available_value_options.append(value_option)

        return available_value_options

    @staticmethod
    def clean_attribute_value_options_field(raw_field: Element) -> tuple[str, str] | tuple[None, None]:
        """Clean a value option fields(it's fields of Справочник)."""
        match get_tag_name(raw_field):
            case 'ИдЗначения':
                return 'bookkeeping_id', raw_field.text
            case 'Значение':
                return 'value', raw_field.text
            case _:
                return None, None
