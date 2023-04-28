from fastapi import APIRouter, Depends, status, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.managers.services_managers import PartnerManager
from src.rest.permissions import is_admin_permissions
from src.rest.schemas.service_entities.partner_schema import PartnerSchema

partner_router = APIRouter(tags=['partners'], prefix='/partners')


@partner_router.get('/', response_model=list[PartnerSchema])
async def get_partners(session: AsyncSession = Depends(get_session)) -> list[PartnerSchema]:
    return await PartnerManager.list(session=session)


@partner_router.post(
    '/',
    response_model=PartnerSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(is_admin_permissions)]
)
async def create_partner(
        file: UploadFile,
        session: AsyncSession = Depends(get_session),
) -> PartnerSchema:
    partner = await PartnerManager.create(input_data={'image': 'tmp'}, session=session)
    file_name = await PartnerManager.upload_file(pk=partner.id, input_file=file)
    partner = await PartnerManager.update(pk=partner.id, input_data={'image': file_name}, session=session)

    return partner


@partner_router.patch(
    '/{partner_id}',
    response_model=PartnerSchema,
    dependencies=[Depends(is_admin_permissions)]
)
async def update_info_about_partner(
        partner_id: int,
        file: UploadFile,
        session: AsyncSession = Depends(get_session)
) -> PartnerSchema:
    await PartnerManager.retrieve(id=partner_id, session=session)
    file_name = await PartnerManager.upload_file(pk=partner_id, input_file=file)
    partner = await PartnerManager.update(
        input_data={'image': file_name},
        pk=partner_id,
        session=session
    )

    return partner


@partner_router.delete(
    '/{partner_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(is_admin_permissions)]
)
async def delete_partner(
        partner_id: int,
        session: AsyncSession = Depends(get_session)
):
    partner: PartnerManager.table = await PartnerManager.retrieve(id=partner_id, session=session)
    result = await PartnerManager.delete(id=partner_id, session=session)  # noqa
    PartnerManager.delete_file(file_name=partner.image)

    return result
