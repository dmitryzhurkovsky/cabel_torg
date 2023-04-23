from fastapi import HTTPException
from sqlalchemy import ColumnOperators, or_, and_, update
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import QueryParams

from src.core.enums import CategoryTypeFilterEnum
from src.rest.managers.base_manager import CRUDManager
from src.rest.managers.product_manager import ProductManager
from src.models.category_model import Category
from src.rest.schemas.category_schema import CategoryUpdateSchema


class CategoryManager(CRUDManager):
    table = Category

    @staticmethod
    def get_filter_expressions(filter_fields: QueryParams) -> list[ColumnOperators]:
        filter_expressions = [Category.is_visible.is_not(False)]

        if type_of_category := filter_fields.get('type_of_category'):
            if type_of_category == CategoryTypeFilterEnum.WITH_DISCOUNT:
                filter_expressions.append(or_(
                    Category.discount.is_not(None),
                    Category.discount != 0
                ))
            elif type_of_category == CategoryTypeFilterEnum.QUICK:
                filter_expressions.append(Category.quick_order.is_not(None))

        return filter_expressions

    @staticmethod
    def get_order_expressions(filter_fields: QueryParams) -> list:
        order_expressions = []
        if type_of_category := filter_fields.get('type_of_category'):
            if type_of_category == CategoryTypeFilterEnum.QUICK:
                order_expressions.append(Category.quick_order)
        else:
            order_expressions.append(Category.order)

        return order_expressions

    @classmethod
    async def filter_list(
            cls,
            filters: QueryParams,
            session: AsyncSession,
            custom_preloaded_fields: tuple | list = (),
            offset: int = 0,
            limit: int = 100
    ) -> list:
        """Get filtered list of objects with pagination."""
        filter_expressions = cls.get_filter_expressions(filters)
        order_by = cls.get_order_expressions(filters)

        return await cls.list(
            session=session,
            where=filter_expressions,
            order_by=order_by,
            custom_preloaded_fields=custom_preloaded_fields,
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
            categories_ids += await cls.get_categories_ids(
                session=session,
                parent_category_ids=subcategories_ids
            )

        return categories_ids

    @classmethod
    async def get_categories_ids_without_discount(cls, pk: int, session: AsyncSession) -> list[int]:
        """
        Get all categories' ids with discounts.
        """
        categories_and_their_subcategories_ids = await cls.get_categories_ids(
            session=session,
            parent_category_ids=[pk],
        )
        query_result = await session.execute(
            select(Category.id).
            where(and_(
                Category.id.in_(categories_and_their_subcategories_ids),
                Category.discount == 0
            ))
        )
        return query_result.scalars().all()  # noqa

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

    @classmethod
    async def set_quick_categories(
            cls,
            categories_ids: list[int],
            session: AsyncSession,
    ):
        """Set quick categories."""
        categories = await cls.list(session=session, where=(Category.quick_order.is_not(None),))
        for category in categories:
            category.quick_order = None
        await session.commit()

        for index, category_id in enumerate(categories_ids, start=1):
            await session.execute(
                update(cls.table).
                where(cls.table.id == category_id).
                values(quick_order=index)
            )

        await session.commit()
