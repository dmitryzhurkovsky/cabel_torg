from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.background import BackgroundTasks

from src.core.db.db import get_session
from src.rest.managers.order_manager import OrderManager
from src.rest.managers.services_managers import DeliveryTypeManager
from src.rest.schemas.order_schema import (
    OrderSchema,
    OrderCreateInputSchema,
    OrderUpdateInputSchema
)
from src.services.auth_service import AuthService
from src.services.order_service import OrderService

order_router = APIRouter(tags=['orders'])


@order_router.get('/orders/mine', response_model=list[OrderSchema])
async def get_my_orders(
        session: AsyncSession = Depends(get_session),
        user=Depends(AuthService.get_current_user)
) -> list[OrderSchema]:
    return await OrderManager.list(session=session, filter_by={'user_id': user.id})


@order_router.get('/orders/{order_id}', response_model=OrderSchema)
async def get_order(
        order_id: int,
        session: AsyncSession = Depends(get_session),
        user=Depends(AuthService.get_current_user)
) -> OrderSchema:
    return await OrderManager.retrieve(id=order_id, session=session)


@order_router.get('/orders', response_model=list[OrderSchema])
async def get_order(
        session: AsyncSession = Depends(get_session),
        user=Depends(AuthService.get_current_user)
) -> list[OrderSchema]:
    return await OrderManager.list(session=session)


@order_router.post('/orders', response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def create_order(
        order_info: OrderCreateInputSchema,
        background_tasks: BackgroundTasks,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> OrderSchema:
    await DeliveryTypeManager.retrieve(id=order_info.delivery_type_id, session=session)  # check if delivery_type exists

    order = await OrderManager.create(
        input_data={
            'user_id': user.id,
            **order_info.__dict__
        },
        session=session
    )
    background_tasks.add_task(func=OrderService.send_create_order, user=user, order=order)
    return order


@order_router.delete(
    '/orders/{order_id}',
    status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
        order_id: int,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    # todo add checking permissions
    await OrderManager.retrieve(
        id=order_id,
        session=session
    )
    await OrderManager.delete(
        id=order_id,
        session=session
    )


@order_router.patch(
    '/orders/{order_id}',
    response_model=OrderSchema,
    status_code=status.HTTP_200_OK)
async def update_product_amount_in_cart(
        order_id: int,
        order_info: OrderUpdateInputSchema,
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
) -> OrderSchema:
    # todo add validation and permissions. An order can be changed only admin or onwer.
    order = await OrderManager.update(
        pk=order_id,
        input_data={**order_info.dict(exclude_unset=True)},
        session=session,
    )
    await OrderService.send_change_order_status(user=user, order=order)

    return order
