from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from src.core.db.db import get_session
from src.rest.managers.watch_list_manager import WatchListManager
from src.rest.schemas.watchlist_schema import (
    WatchListSchema,
    WatchListInputSchema,
    WatchListWithProductSchema
)

watchlist_router = APIRouter(tags=['watch_lists'], prefix='/watch_lists')


@watchlist_router.get(
    '/mine/products',
    response_model=list[WatchListWithProductSchema]  # todo is_owner
)
async def get_product(
        request: Request,
        session: AsyncSession = Depends(get_session),
):
    return await WatchListManager.list(session=session, filter_by={'user_id': request.user.id})


@watchlist_router.post(
    '/mine/products',
    response_model=WatchListSchema,
    status_code=status.HTTP_201_CREATED
)
async def add_product_to_watchlist(
        product_info: WatchListInputSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
) -> WatchListSchema:
    return await WatchListManager.create(
        input_data=WatchListSchema(
            user_id=request.user.id,
            product_id=product_info.product_id
        ),
        session=session
    )


@watchlist_router.delete(
    '/mine/products/{product_id}',
    status_code=status.HTTP_204_NO_CONTENT  # todo add is_owner
)
async def delete_product_from_watchlist(
        product_id: int,
        request: Request,
        session: AsyncSession = Depends(get_session)
):
    await WatchListManager.delete(
        product_id=product_id,
        user_id=request.user.id,
        session=session
    )
