from fastapi import APIRouter, Depends, Query, Request, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.enums import CategoryTypeFilterEnum
from src.rest.managers.category_manager import CategoryManager
from src.rest.schemas.category_schema import (
    CategorySchema,
    CategoryUpdateSchema,
    QuickCategoryCreateSchema
)

category_router = APIRouter(tags=['categories'])


@category_router.get('/categories', response_model=list[CategorySchema])
async def get_categories(
        request: Request,
        session: AsyncSession = Depends(get_session),
        type_of_category: CategoryTypeFilterEnum | None = Query(default=None),
        offset: int = 0, limit: int = Query(default=150, lte=150)
        # todo add norm pagonation
) -> list[CategorySchema]:
    return await CategoryManager.filter_list(
        filters=request.query_params,
        session=session,
        limit=limit,
        offset=offset
    )


@category_router.patch('/categories', response_model=CategorySchema)
async def update_category(
        category_id: int,
        category_info: CategoryUpdateSchema,
        session: AsyncSession = Depends(get_session)
):
    return await CategoryManager.update_discount(
        session=session,
        pk=category_id,
        input_data=category_info
    )


@category_router.post(
    '/categories/set_quick_categories',
    response_model=CategorySchema,
    status_code=status.HTTP_201_CREATED
)
async def update_category(
        quick_categories_info: QuickCategoryCreateSchema,
        session: AsyncSession = Depends(get_session),
):
    await CategoryManager.set_quick_categories(session=session, categories_ids=quick_categories_info.categories)
    return Response(status_code=status.HTTP_201_CREATED)
