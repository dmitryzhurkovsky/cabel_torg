from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.db.db import get_session
from src.core.managers.order_manager import OrderManager
from src.rest.schemas.order_schema import (
    OrderSchema,
    OrderCreateInputSchema
)
from src.services.auth_service import AuthService

order_router = APIRouter(tags=['orders'])


@order_router.get('/orders/mine', response_model=list[OrderSchema])
async def get_orders(
        session: AsyncSession = Depends(get_session),
        user=Depends(AuthService.get_current_user)
) -> list[OrderSchema]:
    return await OrderManager.list(
        session=session,
        filter_fields={'user_id': user.id},
    )


@order_router.post('/orders', response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def create_order(
        order_info: OrderCreateInputSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> OrderSchema:
    return await OrderManager.create(
        input_data={
            'user_id': user.id,
            **order_info.__dict__
        },
        session=session
    )


@order_router.delete(
    '/orders/{order_id}',
    status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
        order_id: int,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    # todo add checking permissions
    await OrderManager.delete(
        id=order_id,
        session=session
    )
