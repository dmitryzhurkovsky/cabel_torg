from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.categories_manager import CategoryManager
from src.rest.schemas.category_schema import CategorySchema

categories_router = APIRouter(tags=['categories'])


@categories_router.get('/categories', response_model=list[CategorySchema])
async def get_categories(
        session: AsyncSession = Depends(get_session)
):
    categories = await CategoryManager.list(session=session)

    return categories
