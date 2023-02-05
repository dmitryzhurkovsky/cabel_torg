from _elementtree import Element
from abc import ABC

from src.core import settings
from src.models.category_model import Category
from src.parser.mixins.base_mixin import BaseMixin
from src.parser.servers import database_service


class CategoryMixin(BaseMixin, ABC):
    EXCLUDED_CATEGORIES = settings.EXCLUDED_CATEGORIES
    DEFAULT_ORDER = settings.DEFAULT_CATEGORIES_ORDER

    @property
    def excluded_categories_cache(self) -> set:
        if not self.CACHE.get('categories'):
            self.CACHE['categories'] = set()
        return self.CACHE['categories']

    async def parse_categories(self):
        """Parse "Категории" node and write then to a database."""
        main_categories = self.root_element[0][3]  # noqa
        await self.clean_category_and_subcategories(raw_categories=main_categories)

    @staticmethod
    def category_has_subcategories(category: Element) -> bool:
        """Check whether an input category has subcategories."""
        return len(category) > 2

    @staticmethod
    def get_subcategories(category: Element) -> Element:
        """Return subcategories of an input category."""
        return category[2]

    async def clean_category_and_subcategories(
            self, raw_categories: Element,
            parent_category_id: int = None,
    ):
        """Parse category's elements and write them to database. It's used recursion for child categories."""
        for raw_category in raw_categories:
            clean_category = self.clean_category_element(element=raw_category)

            # If there is a parent_category_id it means that we parse a subcategory.
            if parent_category_id:
                clean_category |= {'parent_category_id': parent_category_id}

            db_category, _ = await database_service.update_or_create_object(
                db=self.db, refresh=False, update=True, model=Category, fields=clean_category
            )

            # If is_visible is False it means that we shouldn't add show goods and child categories on UI.
            # We put ids of categories in a cache to mountain them later.
            if db_category.is_visible is False:
                self.excluded_categories_cache.add(int(db_category.id))

            if self.category_has_subcategories(category=raw_category):
                await self.db.refresh(db_category)  # noqa

                subcategories = self.get_subcategories(category=raw_category)
                await self.clean_category_and_subcategories(
                    raw_categories=subcategories,
                    parent_category_id=int(db_category.id)
                )

    def clean_category_field(self, raw_field: Element) -> tuple[str, int | str]:
        """A category contains common fields that why we call the clean_common_fields function."""
        return self.clean_common_field(raw_field)

    def clean_category_element(self, element: Element) -> dict:
        """
        Clean an input elements group or an input element of a xml tree
        and transform its fields to "ready to write to a database" state.
        """
        clean_element = {}

        for raw_field in element:
            field_name, field_value = self.clean_category_field(raw_field=raw_field)
            if field_name and field_value:
                clean_element[field_name] = field_value

                # Set up a default value for order attribute it's needed it.
                if order := self.DEFAULT_ORDER.get(field_value) and field_name == 'name':
                    clean_element['order'] = order

        # We shouldn't show some categories on UI.
        clean_element['is_visible'] = False if clean_element.get('name') in self.EXCLUDED_CATEGORIES else True

        return clean_element
