from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.managers.services_managers import FeedbackManager
from src.rest.permissions import is_admin_permission
from src.rest.schemas.service_entities.feedback_schema import (
    FeedbackSchema,
    FeedbackInputSchema
)

feedback_router = APIRouter(tags=['feedbacks'], prefix='/feedbacks')


@feedback_router.get('/', response_model=list[FeedbackSchema])
async def get_feedbacks(session: AsyncSession = Depends(get_session)) -> list[FeedbackSchema]:
    return await FeedbackManager.list(session=session)


@feedback_router.post(
    '',
    response_model=FeedbackSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_feedback(
        feedback_info: FeedbackInputSchema,
        session: AsyncSession = Depends(get_session),
) -> FeedbackSchema:
    return await FeedbackManager.create(
        session=session,
        input_data=feedback_info
    )


@feedback_router.patch(
    '/{feedback_id}',
    response_model=FeedbackSchema)
async def update_info_about_feedback(
        feedback_id: int,
        feedback_info: FeedbackInputSchema,
        session: AsyncSession = Depends(get_session)
) -> FeedbackSchema:
    return await FeedbackManager.update(
        session=session,
        pk=feedback_id,
        input_data=feedback_info.dict(exclude_unset=True)
    )


@feedback_router.delete(
    '/{feedback_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(is_admin_permission)]
)
async def delete_feedback(
        feedback_id: int,
        session: AsyncSession = Depends(get_session)
):
    await FeedbackManager.retrieve(id=feedback_id, session=session)
    return await FeedbackManager.delete(
        session=session,
        id=feedback_id
    )
