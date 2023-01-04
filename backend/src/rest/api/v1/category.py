from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.category_manager import CategoryManager
from src.rest.schemas.category_schema import CategorySchema

category_router = APIRouter(tags=['categories'])


@category_router.get('/categories', response_model=list[CategorySchema])
async def get_categories(
        session: AsyncSession = Depends(get_session)
):
    return await CategoryManager.list(session=session)
