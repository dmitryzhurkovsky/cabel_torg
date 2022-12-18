from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.db.db import get_session
from src.core.managers.cart_manager import CartManager
from src.rest.schemas.cart_schema import (
    ProductInCartSchema,
    ProductInCartCreateSchema,
    ProductInCartUpdateSchema
)
from src.services.auth_service import AuthService

cart_router = APIRouter(tags=['carts'])


@cart_router.post(
    '/carts/mine/products',
    response_model=ProductInCartSchema,
    status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(
        product_info: ProductInCartCreateSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> ProductInCartSchema:
    operation_info = await CartManager.create(
        input_data=ProductInCartSchema(
            user_id=user.id,
            product_id=product_info.product_id,
            amount=product_info.amount
        ),
        session=session
    )
    return operation_info


@cart_router.delete(
    '/carts/mine/products/{product_id}',
    status_code=status.HTTP_204_NO_CONTENT)
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


@cart_router.patch(
    '/carts/mine/products/{product_id}',
    response_model=ProductInCartSchema,
    status_code=status.HTTP_200_OK)
async def update_product_amount_in_cart(
        product_id: int,
        product_info: ProductInCartUpdateSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> ProductInCartSchema:
    operation_info = await CartManager.update_m2m(
        input_data={
            "product_id": product_id,
            "amount": product_info.amount,
            "user_id": user.id},
        session=session,
    )
    return operation_info
