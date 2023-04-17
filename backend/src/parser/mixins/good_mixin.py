from _decimal import Decimal
from _elementtree import Element
from abc import ABC

from sqlalchemy import text

from src.models import Manufacturer, BaseUnit, Category, Attribute
from src.models.attribute_model import AttributeName, AttributeValue, ProductAttribute
from src.models.product_model import Product, ProductStatus
from src.parser.mixins.base_mixin import BaseMixin
from src.parser.servers import database_service
from src.parser.utils import (
    clean_string_from_spaces_and_redundant_symbols,
    clean_fields,
    get_tag_name
)


class GoodsMixin(BaseMixin, ABC):
    # It's a special attribute to find goods under the order.
    # It's initialized in cache_attribute__under_the_order function.
    under_the_order_attribute_id = None

    # It's a special attribute to find goods that shouldn't be uploaded.
    # It's initialized in cache_attribute__do_not_upload_to_site function.
    do_not_upload_to_site_attribute_id = None

    # Service methods
    @property
    def names_cache(self) -> dict:
        """It's used to escape extra queries to a database. We keep ids of AttributeName here."""
        if not self.CACHE.get('names'):
            self.CACHE['names'] = dict()
        return self.CACHE['names']

    @property
    def values_cache(self) -> dict:
        """It's used to escape extra queries to a database. We keep ids of AttributeValue here."""
        if not self.CACHE.get('values'):
            self.CACHE['values'] = dict()
        return self.CACHE['values']

    @property
    def do_not_upload_to_the_site_attribute_cache(self) -> set:
        """
        do_not_upload_to_the_site is used to save ProductAttribute with Attribute.name = 'Не выгружать товар на сайт'.
        We keep ids of ProductAttribute here to check them when we create a product and set is_visible attribute.
        """
        if not self.CACHE.get('attributes'):
            self.CACHE['attributes'] = dict()
        if not self.CACHE['attributes'].get('do_not_upload_to_the_site'):
            self.CACHE['attributes']['do_not_upload_to_the_site'] = set()

        return self.CACHE['attributes']['do_not_upload_to_the_site']

    @property
    def under_the_order_attribute_cache(self) -> set:
        """
        under_the_order is used to save ProductAttribute with Attribute.name = 'Товар под заказ'.
        We keep ids of ProductAttribute here to check them when we create a product and set a suitable status.
        """
        if not self.CACHE.get('attributes'):
            self.CACHE['attributes'] = dict()
        if not self.CACHE['attributes'].get('under_the_order'):
            self.CACHE['attributes']['under_the_order'] = set()

        return self.CACHE['attributes']['under_the_order']

    async def set_under_the_order_attribute_id(self):
        """
        Get AttributeName with name = 'Товар под заказ' and cache its.
        This attribute is used to set a right status for a product during parsing of products.
        """
        query_result = await database_service.get_object(
            db=self.db, model=AttributeName, fields={'payload': 'Товар под заказ'}
        )
        self.under_the_order_attribute_id = query_result.id

    async def set_do_not_upload_to_site_attribute_id(self):
        """
        Get AttributeName with name = 'Не выгружать товар на сайт' and cache its.
        This attribute is used to set a right value for is_visible attribute for a product during parsing of products.
        """
        query_result = await database_service.get_object(
            db=self.db, model=AttributeName, fields={'payload': 'Не выгружать товар на сайт'}
        )
        self.do_not_upload_to_site_attribute_id = query_result.id

    def is_on_the_way_to_the_warehouse(self, attributes: list) -> bool:
        """Check whether a product is on the way to the warehouse."""
        return len(
            {attribute.id for attribute in attributes} &
            self.under_the_order_attribute_cache
        ) > 0

    # Products methods
    async def parse_products(self):
        """Parse "Товары" node and then write them to a database."""
        goods = self.root_element[1][4]  # noqa

        for product in goods:
            clean_product = await self.clean_product(element=product)
            attributes = clean_product.pop('attributes', None)

            product_db, _ = await database_service.update_or_create_object(
                db=self.db,
                model=Product,
                update=True,
                fields=clean_product,
                prefetch_fields=(Product.attributes,),
            )
            if attributes:
                for attribute in attributes:
                    await self.db.refresh(attribute)

                product_db.attributes = attributes
                if self.is_on_the_way_to_the_warehouse(attributes):
                    product_db.status = ProductStatus.ON_THE_WAY_TO_THE_WAREHOUSE

            if is_excluded := clean_product.get('category_id') in self.excluded_categories_cache:  # noqa
                product_db.is_visible = False

            if attributes or is_excluded:
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

    async def clean_product_field(
            self, raw_field: Element
    ) -> tuple[str, int | list | Decimal | None] | tuple[None, None]:
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
            case 'Вес':
                return 'weight', Decimal(raw_field.text)
            case 'Артикул':
                field_name, field_value = 'vendor_code', raw_field.text
            case 'Описание':
                field_name, field_value = 'description', raw_field.text
            case 'Картинка':
                field_name, field_value = 'image_path', raw_field.text[12:]
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
        if full_name == 'Штука':
            full_name = 'Шт.'
        international_abbreviated = raw_field.attrib.get('МеждународноеСокращение')

        fields = clean_fields({
            'code': code,
            'full_name': full_name,
            'international_abbreviated': international_abbreviated
        })

        base_unit, _ = await database_service.update_or_create_object(db=self.db, model=BaseUnit, fields=fields)

        if base_unit:
            return 'base_unit_id', base_unit.id

    async def clean_product_manufacturer(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean a manufacturer(it's Производитель in a xml tree) and
        transform its fields to "ready to write to a database" state.
        """
        manufacturer, _ = await database_service.update_or_create_object(db=self.db, model=Manufacturer, fields={
            'bookkeeping_id': raw_field[0].text,
            'name': raw_field[1].text
        })

        return 'manufacturer_id', manufacturer.id

    async def clean_product_category(self, raw_field: Element) -> tuple[str, int | None] | tuple[None, None]:
        """
        Clean a category(it's Группы in a xml tree) and transform its fields to "ready to write to a database" state.
        """
        category = await database_service.get_object(
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

            db_attribute, _ = await database_service.update_or_create_object(
                db=self.db, model=Attribute, fields={
                    'name_id': name_id_db,
                    'value_id': value_id_db,
                })

            attributes.append(db_attribute)
            if name_id_db == self.do_not_upload_to_site_attribute_id:
                self.do_not_upload_to_the_site_attribute_cache.add(db_attribute.id)
            if name_id_db == self.under_the_order_attribute_id:
                self.under_the_order_attribute_cache.add(db_attribute.id)

        return 'attributes', attributes

    # Attributes methods
    async def parse_attributes(self):
        """
        Clean an attributes's node(it's Свойства in a xml tree) and
        transform its fields to "ready to write to a database" state.
        We write them to names_cache to escape redundant queries to a database.
        """
        attributes = self.root_element[0][4]

        for attribute in attributes:
            bookkeeping_id = attribute[0].text
            payload = attribute[1].text
            value_type = attribute[2].text

            db_attribute_name, _ = await database_service.update_or_create_object(
                db=self.db, model=AttributeName, fields={
                    'bookkeeping_id': bookkeeping_id,
                    'payload': payload
                })

            self.names_cache[bookkeeping_id] = db_attribute_name.id

            if value_type == 'Справочник':
                await self.clean_available_options(attribute[3])

        await self.set_under_the_order_attribute_id()
        await self.set_do_not_upload_to_site_attribute_id()

    async def clean_available_options(self, available_values: Element):
        """
        Clean an available_options(it's ВариантыЗначений in a xml tree) and
        transform its fields to "ready to write to a database" state.
        We write them to values_cache to escape redundant queries to a database.
        """
        for value in available_values:
            bookkeeping_id = value[0].text
            payload = value[1].text

            db_attribute_value, _ = await database_service.update_or_create_object(
                db=self.db, model=AttributeValue, fields={
                    'bookkeeping_id': bookkeeping_id,
                    'payload': payload
                })

            self.values_cache[bookkeeping_id] = db_attribute_value.id

    async def set_is_visible_attribute(self):
        """Set is_visible attribute after parsing all product's attributes."""

        await self.db.execute(
            text(f"""
            update products
            set is_visible = True
            from products p
            join product_attribute pa on p.id = pa.product_id
            where pa.attribute_id in ({", ".join((str(el) for el in self.do_not_upload_to_the_site_attribute_cache))})
            """)
        )
