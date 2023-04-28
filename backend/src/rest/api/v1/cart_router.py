from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request

from src.core.db.db import get_session
from src.rest.managers.cart_manager import CartManager
from src.rest.managers.product_manager import ProductManager
from src.rest.schemas.cart_schema import (
    CartSchema,
    CartCreateInputSchema,
    CartUpdateInputSchema,
    CartWithProductSchema
)

cart_router = APIRouter(tags=['carts'], prefix='/carts')


@cart_router.get('/mine/products', response_model=list[CartWithProductSchema])
async def get_product(
        request: Request,
        session: AsyncSession = Depends(get_session),
) -> list[CartWithProductSchema]:
    return await CartManager.list(session=session, filter_by={'user_id': request.user.id})


@cart_router.post(
    '/mine/products',
    response_model=CartSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_product_to_cart(
        product_info: CartCreateInputSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
) -> CartSchema:
    return await CartManager.create(
        input_data=CartSchema(
            user_id=request.user.id,
            product_id=product_info.product_id,
            amount=product_info.amount
        ),
        session=session
    )


@cart_router.delete(
    '/mine/products/{product_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
# todo add is_owner
async def delete_product_from_cart(
        product_id: int,
        request: Request,
        session: AsyncSession = Depends(get_session)
):
    await ProductManager.retrieve(id=product_id, session=session)
    await CartManager.delete(
        product_id=product_id,
        user_id=request.user.id,
        session=session
    )


@cart_router.patch(
    '/mine/products/{product_id}',
    response_model=CartSchema,
    status_code=status.HTTP_200_OK
)
# todo add is_owner
async def update_product_amount_in_cart(
        product_id: int,
        product_info: CartUpdateInputSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
) -> CartSchema:
    return await CartManager.update_m2m(
        input_data=CartSchema(
            product_id=product_id,
            amount=product_info.amount,
            user_id=request.user.id),
        session=session,
    )
