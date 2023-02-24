from fastapi import APIRouter, Depends, status, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.managers.services_managers import PartnerManager
from src.rest.schemas.service_entities.partner_schema import PartnerSchema

partner_router = APIRouter(tags=['partners'])


@partner_router.get('/partners', response_model=list[PartnerSchema])
async def get_partners(session: AsyncSession = Depends(get_session)) -> list[PartnerSchema]:
    return await PartnerManager.list(session=session)


@partner_router.post('/partners', response_model=PartnerSchema, status_code=status.HTTP_201_CREATED)
async def create_partner(
        file: UploadFile,
        session: AsyncSession = Depends(get_session),
) -> PartnerSchema:
    partner = await PartnerManager.create(input_data={'image': 'tmp'}, session=session)
    file_name = await PartnerManager.upload_file(pk=partner.id, input_file=file)
    await PartnerManager.update(pk=partner.id, input_data={'image': file_name}, session=session)
    await session.refresh(partner)

    return partner


@partner_router.patch('/partners/{partner_id}', response_model=PartnerSchema)
async def update_info_about_partner(
        partner_id: int,
        file: UploadFile,
        session: AsyncSession = Depends(get_session)
) -> PartnerSchema:
    file_name = await PartnerManager.upload_file(pk=partner_id, input_file=file)
    partner = await PartnerManager.update(pk=partner_id, session=session)
    await session.refresh(partner)

    return partner


@partner_router.delete('/partners/{partner_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_partner(
        partner_id: int,
        session: AsyncSession = Depends(get_session)
):
    result = await PartnerManager.delete(id=partner_id, session=session)
    PartnerManager.delete_file(pk=partner_id)

    return result

