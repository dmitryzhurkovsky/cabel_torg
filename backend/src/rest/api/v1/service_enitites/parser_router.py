from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.managers.services_managers import VendorInfoManager
from src.rest.schemas.service_entities.parser_info_schema import ParserInfoSchema

parser_info_router = APIRouter(tags=['parser_info'], prefix='/parser_info')


@parser_info_router.get('/1', response_model=ParserInfoSchema)
async def get_vendor_info(
        session: AsyncSession = Depends(get_session)
) -> ParserInfoSchema:
    return await VendorInfoManager.retrieve(id=1, session=session)
