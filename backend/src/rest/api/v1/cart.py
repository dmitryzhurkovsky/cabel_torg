from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.db.db import get_session
from src.core.managers.cart_manager import CartManager
from src.rest.schemas.watchlist_schema import (
    ProductInWatchListSchema,
    ProductInWatchListInputSchema
)
from src.services.auth_service import AuthService

cart_router = APIRouter(tags=['carts'])


@cart_router.post('/carts/mine/products', response_model=ProductInWatchListSchema, status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(
        operation_info: ProductInWatchListInputSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> ProductInWatchListSchema:
    operation_info.user_id = user.id
    operation_info = await CartManager.create(
        input_data=operation_info,
        session=session
    )
    return operation_info


@cart_router.delete('/carts/mine/products/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_from_cart(
        product_id: int,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    await CartManager.delete(
        product_id=product_id,
        user_id=user.id,
        session=session
    )


#  todo
@cart_router.patch('/carts/mine/products/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_product_amount_in_cart(
        operation_info: ProductInWatchListInputSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    operation_info = await CartManager.update(
        input_data=operation_info,
        session=session
    )
