from _elementtree import Element

from mixins.base_mixin import BaseMixin
from src.core.db import database_services

from src.models.category_model import Category


class CategoryMixin(BaseMixin):
    async def parse_categories(self):
        """Parse "Категории" node and write then to a database."""
        main_categories = self.ROOT_ELEMENT[0][3]  # noqa
        await self.parse_category_and_subcategories(raw_categories=main_categories)

    @staticmethod
    def category_has_subcategories(category: Element) -> bool:
        """Check whether an input category has subcategories."""
        return len(category) > 2

    @staticmethod
    def get_subcategories(category: Element) -> Element:
        """Return subcategories of an input category."""
        return category[2]

    async def parse_category_and_subcategories(
            self, raw_categories: Element,
            parent_category_id: int = None,
    ):
        """Parse category's elements and write them to database. It used recursion for child categories."""
        for raw_category in raw_categories:
            clean_category = self.clean_category_element(element=raw_category)

            if parent_category_id:
                clean_category |= {'parent_category_id': parent_category_id}

            db_category, _ = await database_services.get_or_create(
                db=self.db, model=Category, fields=clean_category  # noqa
            )

            if self.category_has_subcategories(category=raw_category):
                await self.db.refresh(db_category)  # noqa

                subcategories = self.get_subcategories(category=raw_category)
                await self.parse_category_and_subcategories(
                    raw_categories=subcategories, parent_category_id=int(db_category.id)
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

        return clean_element
