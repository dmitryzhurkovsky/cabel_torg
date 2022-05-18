from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.categories_manager import CategoryManager
from src.rest.schemas.category_schema import CategoryWithNestedCategoriesSchema

categories_router = APIRouter(tags=['categories'])


@categories_router.get('/categories', response_model=list[CategoryWithNestedCategoriesSchema])
async def get_categories(session: AsyncSession = Depends(get_session)):
    categories = await CategoryManager.list(
        session=session,
        prefetch_fields=(CategoryManager.table.subcategories,)
    )

    return categories
