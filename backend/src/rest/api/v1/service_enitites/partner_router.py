from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.services_managers import PartnerManager
from src.rest.schemas.service_entities.partner_schema import PartnerSchema, PartnerInputSchema

partner_router = APIRouter(tags=['partners'])


@partner_router.get('/partners', response_model=list[PartnerSchema])
async def get_partners(session: AsyncSession = Depends(get_session)) -> list[PartnerSchema]:
    return await PartnerManager.list(session=session)


@partner_router.post('/partners', response_model=PartnerSchema, status_code=status.HTTP_201_CREATED)
async def create_partner(
        partner_info: PartnerInputSchema,
        session: AsyncSession = Depends(get_session),
) -> PartnerSchema:
    return await PartnerManager.create(
        session=session,
        input_data=partner_info
    )


@partner_router.patch('/partners/{partner_id}', response_model=PartnerSchema)
async def update_info_about_partner(
        partner_id: int,
        partner_info: PartnerInputSchema,
        session: AsyncSession = Depends(get_session)
) -> PartnerSchema:
    return await PartnerManager.update(
        session=session, pk=partner_id, input_data=partner_info.dict(exclude_unset=True)
    )


@partner_router.delete('/partners/{partner_id}', status_code=status.HTTP_204_NO_CONTENT)
async def create_partner(
        partner_id: int,
        session: AsyncSession = Depends(get_session)
):
    return await PartnerManager.delete(
        session=session,
        id=partner_id
    )
