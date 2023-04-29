from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.background import BackgroundTasks
from starlette.requests import Request

from src.core.db.db import get_session
from src.rest.managers.order_manager import OrderManager
from src.rest.managers.services_managers import DeliveryTypeManager
from src.rest.permissions import is_admin_permission, is_authenticated_permission
from src.rest.schemas.order_schema import (
    OrderSchema,
    OrderCreateInputSchema,
    OrderUpdateInputSchema
)
from src.services.order_service import OrderService

order_router = APIRouter(tags=['orders'], prefix='/orders')


@order_router.get(
    '/mine',
    response_model=list[OrderSchema],
    dependencies=[Depends(is_authenticated_permission)]
)
async def get_my_orders(
        request: Request,
        session: AsyncSession = Depends(get_session),
) -> list[OrderSchema]:
    return await OrderManager.list(session=session, filter_by={'user_id': request.user.id})


@order_router.get(
    '/{order_id}',
    response_model=OrderSchema,
    dependencies=[Depends(is_admin_permission)]
)
async def get_order(
        order_id: int,
        session: AsyncSession = Depends(get_session),
) -> OrderSchema:
    return await OrderManager.retrieve(id=order_id, session=session)


@order_router.get(
    '/orders',
    response_model=list[OrderSchema],
    dependencies=[Depends(is_admin_permission)]
)
async def get_order(session: AsyncSession = Depends(get_session)) -> list[OrderSchema]:
    return await OrderManager.list(session=session)


@order_router.post(
    '/',
    response_model=OrderSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(is_authenticated_permission)]
)
async def create_order(
        order_info: OrderCreateInputSchema,
        request: Request,
        background_tasks: BackgroundTasks,
        session: AsyncSession = Depends(get_session)
) -> OrderSchema:
    await DeliveryTypeManager.retrieve(id=order_info.delivery_type_id, session=session)  # check if delivery_type exists

    order = await OrderManager.create(
        input_data={
            'user_id': request.user.id,
            **order_info.__dict__
        },
        session=session
    )
    background_tasks.add_task(func=OrderService.send_create_order, user=request.user, order=order)
    return order


@order_router.delete(
    '/{order_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(is_admin_permission)]
)
async def delete_order(
        order_id: int,
        session: AsyncSession = Depends(get_session)
):
    await OrderManager.retrieve(
        id=order_id,
        session=session
    )
    await OrderManager.delete(
        id=order_id,
        session=session
    )


@order_router.patch(
    '/{order_id}',
    response_model=OrderSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(is_admin_permission)]
)
async def update_product_amount_in_cart(
        order_id: int,
        order_info: OrderUpdateInputSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
) -> OrderSchema:
    order = await OrderManager.update(
        pk=order_id,
        input_data={**order_info.dict(exclude_unset=True)},
        session=session,
    )
    await OrderService.send_change_order_status(user=request.user, order=order)

    return order
