from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.watch_list_manager import WatchListManager
from src.rest.schemas.watchlist_schema import ProductInWatchListSchema
from src.services.auth_service import AuthService

watchlist_router = APIRouter(tags=['watch_lists'])


@watchlist_router.post('/watch_lists', response_model=ProductInWatchListSchema, status_code=status.HTTP_201_CREATED)
async def add_product_to_watchlist(
        product_info: ProductInWatchListSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> ProductInWatchListSchema:
    product_info.user_id = user.id
    operation_info = await WatchListManager.create(
        input_data=product_info,
        session=session
    )
    return operation_info


@watchlist_router.delete('/watch_lists/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_from_watchlist(
        product_id: int,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    await WatchListManager.delete(
        product_id=product_id,
        user_id=user.id,
        session=session
    )
