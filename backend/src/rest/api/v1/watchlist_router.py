from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.watch_list_manager import WatchListManager
from src.rest.schemas.watchlist_schema import (
    WatchListSchema,
    WatchListInputSchema, WatchListWithProductSchema
)
from src.services.auth_service import AuthService

watchlist_router = APIRouter(tags=['watch_lists'])


@watchlist_router.get('/watch_lists/mine/products', response_model=list[WatchListWithProductSchema])
async def get_product(
        session: AsyncSession = Depends(get_session),
        user=Depends(AuthService.get_current_user)
):
    return await WatchListManager.list(session=session, filter_by={'user_id': user.id})


@watchlist_router.post(
    '/watch_lists/mine/products',
    response_model=WatchListSchema,
    status_code=status.HTTP_201_CREATED)
async def add_product_to_watchlist(
        product_info: WatchListInputSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> WatchListSchema:
    return await WatchListManager.create(
        input_data=WatchListSchema(
            user_id=user.id,
            product_id=product_info.product_id
        ),
        session=session
    )


@watchlist_router.delete(
    '/watch_lists/mine/products/{product_id}',
    status_code=status.HTTP_204_NO_CONTENT)
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
