from fastapi import APIRouter, Depends, Query, Request, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.enums import CategoryTypeFilterEnum
from src.rest.managers.category_manager import CategoryManager
from src.rest.permissions import is_admin_permission
from src.rest.schemas.category_schema import (
    CategorySchema,
    CategoryUpdateSchema,
    QuickCategoryCreateSchema
)

category_router = APIRouter(tags=['categories'], prefix='/categories')


@category_router.get('', response_model=list[CategorySchema])
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


@category_router.get('/{category_id:path}', response_model=CategorySchema)
async def get_category(
        category_id: int | str,
        session: AsyncSession = Depends(get_session)
):
    return await CategoryManager.retrieve(
        id=category_id,
        site_link=category_id,
        use_or_condition=True,
        session=session
    )


@category_router.patch(
    '/{category_id}',
    response_model=CategorySchema,
    dependencies=[Depends(is_admin_permission)]
)
async def update_category(
        category_id: int,
        category_info: CategoryUpdateSchema,
        session: AsyncSession = Depends(get_session)
):
    await CategoryManager.retrieve(id=category_id, session=session)

    return await CategoryManager.update_discount(
        session=session,
        pk=category_id,
        input_data=category_info
    )


@category_router.post(
    '/set_quick_categories',
    response_model=CategorySchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(is_admin_permission)]
)
async def update_category(
        quick_categories_info: QuickCategoryCreateSchema,
        session: AsyncSession = Depends(get_session),
):
    await CategoryManager.set_quick_categories(session=session, categories_ids=quick_categories_info.categories)
    return Response(status_code=status.HTTP_201_CREATED)
