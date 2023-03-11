from fastapi import APIRouter, Depends, status, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.managers.product_manager import ProductManager
from src.rest.managers.services_managers import RequestCallManager
from src.models.service_entities.request_call_model import RequestCallType
from src.rest.schemas.service_entities.request_call_schema import (
    RequestCallInputSchema,
    RequestCallSchema
)

request_call_router = APIRouter(tags=['request_calls'])


@request_call_router.get('/request_calls', response_model=list[RequestCallSchema])
async def get_request_calls(
        request: Request,
        type_of_request_call: RequestCallType | None = Query(
            description=RequestCallType.description(), default=RequestCallType.UNSET
        ),
        session: AsyncSession = Depends(get_session)
) -> list[RequestCallSchema]:
    return await RequestCallManager.filter_list(filters=request.query_params, session=session)


@request_call_router.post(
    '/request_calls',
    response_model=RequestCallSchema,
    status_code=status.HTTP_201_CREATED)
async def create_request_call(
        request_call_info: RequestCallInputSchema,
        session: AsyncSession = Depends(get_session),
) -> RequestCallSchema:
    if product_id := request_call_info.product_id:
        await ProductManager.retrieve(id=product_id)

    return await RequestCallManager.create(
        session=session,
        input_data=request_call_info
    )


@request_call_router.patch(
    '/request_calls/{request_call_id}',
    response_model=RequestCallSchema)
async def update_info_about_feedback(
        request_call_id: int,
        request_call_info: RequestCallInputSchema,
        session: AsyncSession = Depends(get_session)
) -> RequestCallSchema:
    return await RequestCallManager.update(
        session=session,
        pk=request_call_id,
        input_data=request_call_info.dict(exclude_unset=True)
    )


@request_call_router.delete(
    '/request_calls/{request_call_id}',
    status_code=status.HTTP_204_NO_CONTENT)
async def delete_request_call(
        request_call_id: int,
        session: AsyncSession = Depends(get_session)
):
    await RequestCallManager.retrieve(id=request_call_id, session=session)
    return await RequestCallManager.delete(
        session=session,
        id=request_call_id
    )
