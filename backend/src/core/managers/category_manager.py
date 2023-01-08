from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.delete_mixin import DeleteMixin
from src.core.db.mixins.list_mixin import ListMixin
from src.core.db.mixins.retrieve_mixin import RetrieveMixin
from src.models.category_model import Category


class CategoryManager(ListMixin, RetrieveMixin, DeleteMixin):
    table = Category

    @classmethod
    async def get_categories_ids(
            cls, session: AsyncSession, parent_category_ids: tuple | list
    ):
        """
        Since we have a FK to a parent category we have to make extra queries to get
        subcategories ids for filtering by a category_id.
        """
        categories_ids = parent_category_ids

        result = await session.execute(
            select(Category.id).
            filter(Category.parent_category_id.in_(parent_category_ids))
        )
        subcategories_ids = result.scalars().all()

        if subcategories_ids:
            categories_ids += await cls.get_categories_ids(session=session, parent_category_ids=subcategories_ids)

        return categories_ids
