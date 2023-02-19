from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.exception.base_exception import BadRequestError
from src.managers.services_managers import VendorInfoManager, AddressManager
from src.rest.schemas.service_entities.vendor_info_schema import (
    VendorInfoSchema,
    VendorInfoInputSchema,
    AddressSchema,
    AddressInputSchema
)

vendor_info_router = APIRouter(tags=['vendor_info'])


@vendor_info_router.get('/vendor_info/1/', response_model=VendorInfoSchema)
async def get_vendor_info(
        session: AsyncSession = Depends(get_session)
) -> VendorInfoSchema:
    vendor = await VendorInfoManager.list(session=session)
    if vendor and vendor[0]:
        return vendor[0]

    return []


@vendor_info_router.post(
    '/vendor_info',
    response_model=VendorInfoSchema,
    status_code=status.HTTP_201_CREATED)
async def create_vendor_info(
        vendor_info: VendorInfoInputSchema,
        session: AsyncSession = Depends(get_session),
) -> VendorInfoSchema:
    vendor = await VendorInfoManager.list(session=session)
    if vendor and vendor[0]:
        raise BadRequestError(detail='The instance of vendor info already exists.')

    return await VendorInfoManager.create(
        session=session,
        input_data=vendor_info
    )


@vendor_info_router.patch(
    '/vendor_info/1/',
    response_model=VendorInfoSchema)
async def update_info_about_delivery_type(
        delivery_type_info: VendorInfoInputSchema,
        session: AsyncSession = Depends(get_session)
) -> VendorInfoSchema:
    vendor = await VendorInfoManager.list(session=session)
    if vendor and vendor[0]:
        pk = vendor[0].id
    else:
        raise BadRequestError(detail='You should create any instance of vendor before update something.')

    return await VendorInfoManager.update(
        session=session,
        pk=pk,
        input_data=delivery_type_info.dict(exclude_unset=True)
    )


@vendor_info_router.get('/vendor_info/1/addresses', response_model=list[AddressSchema])
async def get_addresses(
        session: AsyncSession = Depends(get_session)
) -> list[AddressSchema]:
    vendor = await VendorInfoManager.list(session=session)
    if vendor and vendor[0]:
        vendor_id = vendor[0].id
    else:
        raise BadRequestError(detail='You should create any instance of vendor before update something.')

    return await AddressManager.list(filter_by={'vendor_info_id': vendor_id}, session=session)


@vendor_info_router.post(
    '/vendor_info/1/addresses',
    response_model=AddressSchema,
    status_code=status.HTTP_201_CREATED)
async def create_address(
        vendor_info: AddressInputSchema,
        session: AsyncSession = Depends(get_session),
) -> AddressSchema:
    vendor = await VendorInfoManager.list(session=session)
    if vendor and vendor[0]:
        vendor_id = vendor[0].id
    else:
        raise BadRequestError(detail='You should create any instance of vendor before update something.')

    return await AddressManager.create(
        session=session,
        input_data={
            'vendor_info_id': vendor_id,
            **vendor_info.__dict__
        }
    )


@vendor_info_router.patch(
    '/vendor_info/1/addresses/{address_id}',
    response_model=AddressSchema)
async def update_info_about_address(
        address_id: int,
        delivery_type_info: AddressInputSchema,
        session: AsyncSession = Depends(get_session)
) -> AddressSchema:
    return await AddressManager.update(
        session=session,
        pk=address_id,
        input_data=delivery_type_info.dict(exclude_unset=True)
    )


@vendor_info_router.delete(
    '/vendor_info/1/addresses/{address_id}',
    status_code=status.HTTP_204_NO_CONTENT)
async def delete_addresses(
        address_id: int,
        session: AsyncSession = Depends(get_session)
):
    return await AddressManager.delete(
        session=session,
        id=address_id
    )
