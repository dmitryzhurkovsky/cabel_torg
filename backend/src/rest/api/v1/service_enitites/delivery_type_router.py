from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.managers.services_managers import DeliveryTypeManager
from src.rest.permissions import is_admin_permission
from src.rest.schemas.service_entities.delivery_type_schema import (
    DeliveryTypeSchema,
    DeliveryTypeInputSchema
)

delivery_type_router = APIRouter(tags=['delivery_types'], prefix='/delivery_types')


@delivery_type_router.get('', response_model=list[DeliveryTypeSchema])
async def get_delivery_types(session: AsyncSession = Depends(get_session)) -> list[DeliveryTypeSchema]:
    return await DeliveryTypeManager.list(session=session)


@delivery_type_router.post(
    '',
    response_model=DeliveryTypeSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(is_admin_permission)]
)
async def create_delivery_type(
        delivery_type_info: DeliveryTypeInputSchema,
        session: AsyncSession = Depends(get_session),
) -> DeliveryTypeSchema:
    return await DeliveryTypeManager.create(
        session=session,
        input_data=delivery_type_info
    )


@delivery_type_router.patch(
    '/{delivery_type_id}',
    response_model=DeliveryTypeSchema,
    dependencies=[Depends(is_admin_permission)]
)
async def update_info_about_delivery_type(
        delivery_type_id: int,
        delivery_type_info: DeliveryTypeInputSchema,
        session: AsyncSession = Depends(get_session)
) -> DeliveryTypeSchema:
    return await DeliveryTypeManager.update(
        session=session,
        pk=delivery_type_id,
        input_data=delivery_type_info.dict(exclude_unset=True)
    )


@delivery_type_router.delete(
    '/{delivery_type_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(is_admin_permission)]
)
async def delete_delivery_type(
        delivery_type_id: int,
        session: AsyncSession = Depends(get_session)
):
    await DeliveryTypeManager.retrieve(
        session=session,
        id=delivery_type_id
    )
    return await DeliveryTypeManager.delete(
        session=session,
        id=delivery_type_id
    )
