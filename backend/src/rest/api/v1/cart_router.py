from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.db.db import get_session
from src.managers.cart_manager import CartManager
from src.managers.product_manager import ProductManager
from src.rest.schemas.cart_schema import (
    CartSchema,
    CartCreateInputSchema,
    CartUpdateInputSchema,
    CartWithProductSchema
)
from src.services.auth_service import AuthService

cart_router = APIRouter(tags=['carts'])


@cart_router.get('/carts/mine/products', response_model=list[CartWithProductSchema])
async def get_product(
        session: AsyncSession = Depends(get_session),
        user=Depends(AuthService.get_current_user)
) -> list[CartWithProductSchema]:
    return await CartManager.list(session=session, filter_by={'user_id': user.id})


@cart_router.post(
    '/carts/mine/products',
    response_model=CartSchema,
    status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(
        product_info: CartCreateInputSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> CartSchema:
    return await CartManager.create(
        input_data=CartSchema(
            user_id=user.id,
            product_id=product_info.product_id,
            amount=product_info.amount
        ),
        session=session
    )


@cart_router.delete(
    '/carts/mine/products/{product_id}',
    status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_from_cart(
        product_id: int,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    await ProductManager.retrieve(id=product_id, session=session)
    await CartManager.delete(
        product_id=product_id,
        user_id=user.id,
        session=session
    )


@cart_router.patch(
    '/carts/mine/products/{product_id}',
    response_model=CartSchema,
    status_code=status.HTTP_200_OK)
async def update_product_amount_in_cart(
        product_id: int,
        product_info: CartUpdateInputSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> CartSchema:
    return await CartManager.update_m2m(
        input_data=CartSchema(
            product_id=product_id,
            amount=product_info.amount,
            user_id=user.id),
        session=session,
    )
