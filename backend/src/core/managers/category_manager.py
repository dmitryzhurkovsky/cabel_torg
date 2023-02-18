from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.managers.base_manager import CRUDManager
from src.core.managers.product_manager import ProductManager
from src.models.category_model import Category
from src.rest.schemas.category_schema import CategoryUpdateSchema


class CategoryManager(CRUDManager):
    table = Category

    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            filter_by: dict = {},
            where: tuple | list = (),
            order_fields: tuple | list = (),
            offset: int = 0,
            limit: int = 100
    ) -> list:
        return await super().list(
            session=session,
            where=(Category.is_visible.is_not(False),),
            offset=offset,
            limit=limit
        )

    @classmethod
    async def get_categories_ids(
            cls,
            parent_category_ids: list,
            session: AsyncSession
    ):
        """
        Since we have a FK to a parent category we have to make extra queries to get
        subcategories ids for filtering by a category_id.
        """
        categories_ids = parent_category_ids

        query_result = await session.execute(
            select(Category.id).
            where(Category.parent_category_id.in_(parent_category_ids))
        )
        subcategories_ids = query_result.scalars().all()

        if subcategories_ids:
            categories_ids += await cls.get_categories_ids(session=session, parent_category_ids=subcategories_ids)

        return categories_ids

    @classmethod
    async def get_categories_ids_without_discount(cls, pk: int, session: AsyncSession):
        """
        Get all categories' ids with discounts.
        """
        categories_and_their_subcategories_ids = await cls.get_categories_ids(
            session=session,
            parent_category_ids=[pk],
        )
        query_result = await session.execute(
            select(Category.id).
            where(
                Category.id.in_(categories_and_their_subcategories_ids),
                Category.discount == 0
            )
        )
        return query_result.scalars().all()

    @classmethod
    async def update_discount(
            cls,
            pk: int,
            input_data: CategoryUpdateSchema,
            session: AsyncSession,
    ) -> Category | HTTPException:
        """
        Update category's discount and prices of products in the category and its subcategories.
        """
        categories_ids_without_discount = await cls.get_categories_ids_without_discount(pk=pk, session=session)
        await ProductManager.bulk_update_discounts(
            categories_ids=categories_ids_without_discount,
            discount=input_data.discount,
            session=session
        )

        category = await cls.update(pk=pk, session=session, input_data=input_data)
        return category
