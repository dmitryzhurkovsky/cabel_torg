from _elementtree import Element

from src.models.attribute_model import AttributeValue, AttributeName
from src.parser.mixins.base_mixin import BaseMixin
from src.core.db import database_services
from src.core.utils import (
    clean_string_from_spaces_and_redundant_symbols,
    clean_fields,
    get_tag_name
)
from src.models import Manufacturer, BaseUnit, Category, Attribute

from src.models.product_models import Product


class GoodsMixin(BaseMixin):
    @property
    def names_cache(self) -> dict:
        if not self.CACHE.get('names'):
            self.CACHE['names'] = dict()
        return self.CACHE['names']

    @property
    def values_cache(self) -> dict:
        if not self.CACHE.get('values'):
            self.CACHE['values'] = dict()
        return self.CACHE['values']

    async def parse_products(self):
        """Parse "Товары" node and then write them to a database."""
        goods = self.ROOT_ELEMENT[1][4]  # noqa

        for product in goods:
            attributes = None

            clean_product = await self.clean_product(element=product)
            if clean_product.get('attributes'):
                attributes = clean_product.pop('attributes')

            product_db, _ = await database_services.get_or_create(
                db=self.db, model=Product, fields=clean_product, prefetch_fields=('attributes',)
            )

            if attributes:  # todo maybe there is better way to do it?
                for attribute in attributes:
                    if attribute not in product_db.attributes:
                        product_db.attributes.append(attribute)
            await self.db.commit()

    async def clean_product(self, element: Element) -> dict:
        """
        Clean a product(it's Товар in a xml tree) and transform its fields
        to "ready to write to a database" state.
        """
        product = {}
        product_images = []

        for raw_field in element:
            field_name, field_value = await self.clean_product_field(raw_field=raw_field)
            if field_name and field_value:
                if field_name == 'image_path':
                    product_images.append(field_value)
                else:
                    product[field_name] = field_value

        product['images'] = ",".join(image for image in product_images)

        return product

    async def clean_product_field(self, raw_field: Element) -> tuple[str, int | list | None] | tuple[None, None]:
        """
        Convert raw fields that are called by Russian language to an English alternative and
        if it's required make a query to a database to get id of a nested model.
        """
        field_name, field_value = self.clean_common_field(raw_field=raw_field)

        if field_name and field_value:
            return field_name, field_value

        match get_tag_name(raw_field):  # todo make it by dict
            case 'БазоваяЕдиница':
                return await self.clean_product_base_unit(raw_field=raw_field)
            case 'Изготовитель':
                return await self.clean_product_manufacturer(raw_field=raw_field)
            case 'Группы':
                return await self.clean_product_category(raw_field=raw_field)
            case 'ЗначенияСвойств':
                return await self.clean_product_attributes(raw_field=raw_field)
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
        return None, None

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
            db=self.db, model=BaseUnit, fields=fields
        )
        await self.db.refresh(base_unit)

        if base_unit:
            return 'base_unit_id', base_unit.id

    async def clean_product_manufacturer(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean a manufacturer(it's Производитель in a xml tree) and
        transform its fields to "ready to write to a database" state.
        """
        manufacturer, _ = await database_services.get_or_create(
            db=self.db, model=Manufacturer, fields={
                'bookkeeping_id': raw_field[0].text,
                'name': raw_field[1].text
            })
        await self.db.refresh(manufacturer)

        return 'manufacturer_id', manufacturer.id

    async def clean_product_category(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean a category(it's Группы in a xml tree) and transform its fields to "ready to write to a database" state.
        """
        category = await database_services.get(
            db=self.db, model=Category, fields={'bookkeeping_id': raw_field[0].text}
        )

        if category:
            return 'category_id', category.id

    async def clean_product_attributes(self, raw_field: Element) -> tuple[str, list]:
        """
        Clean an attributes(it's ЗначенияСвойств in a xml tree) and
        transform its fields to "ready to write to a database" state.
        """
        attributes = []

        for product_attribute in raw_field:
            name_bookkeeping_id = product_attribute[0].text
            value_bookkeeping_id = product_attribute[1].text

            name_id_db = self.names_cache.get(name_bookkeeping_id)
            value_id_db = self.values_cache.get(value_bookkeeping_id)

            db_attribute, _ = await database_services.get_or_create(
                db=self.db, model=Attribute, fields={
                    'name_id': name_id_db,
                    'value_id': value_id_db,
                })
            await self.db.refresh(db_attribute)

            attributes.append(db_attribute)

        return 'attributes', attributes

    async def parse_attributes(self):
        """
        Clean an attributes's node(it's Свойства in a xml tree) and
        transform its fields to "ready to write to a database" state.
        We write them to names_cache to escape redundant queries to a database.
        """
        attributes = self.ROOT_ELEMENT[0][4]

        for attribute in attributes:
            bookkeeping_id = attribute[0].text
            payload = attribute[1].text
            value_type = attribute[2].text

            db_attribute_name, _ = await database_services.get_or_create(
                db=self.db, model=AttributeName, fields={
                    'bookkeeping_id': bookkeeping_id,
                    'payload': payload
                })
            await self.db.refresh(db_attribute_name)

            self.names_cache[bookkeeping_id] = db_attribute_name.id

            if value_type == 'Справочник':
                await self.clean_available_options(attribute[3])

    async def clean_available_options(self, available_values: Element):
        """
        Clean an available_options(it's ВариантыЗначений in a xml tree) and
        transform its fields to "ready to write to a database" state.
        We write them to values_cache to escape redundant queries to a database.
        """
        for value in available_values:
            bookkeeping_id = value[0].text
            payload = value[1].text

            db_attribute_value, _ = await database_services.get_or_create(
                db=self.db, model=AttributeValue, fields={
                    'bookkeeping_id': bookkeeping_id,
                    'payload': payload
                })
            await self.db.refresh(db_attribute_value)

            self.values_cache[bookkeeping_id] = db_attribute_value.id