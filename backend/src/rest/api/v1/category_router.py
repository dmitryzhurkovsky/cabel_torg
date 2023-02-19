from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.managers.category_manager import CategoryManager
from src.rest.schemas.category_schema import CategorySchema, CategoryUpdateSchema

category_router = APIRouter(tags=['categories'])


@category_router.get('/categories', response_model=list[CategorySchema])
async def get_categories(
        session: AsyncSession = Depends(get_session)
):
    return await CategoryManager.list(session=session)


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
