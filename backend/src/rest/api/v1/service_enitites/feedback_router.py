from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.managers.services_managers import FeedbackManager
from src.rest.schemas.service_entities.feedback_schema import (
    FeedbackSchema,
    FeedbackInputSchema
)

feedback_router = APIRouter(tags=['feedbacks'])


@feedback_router.get('/feedbacks', response_model=list[FeedbackSchema])
async def get_feedbacks(session: AsyncSession = Depends(get_session)) -> list[FeedbackSchema]:
    return await FeedbackManager.list(session=session)


@feedback_router.post(
    '/feedbacks',
    response_model=FeedbackSchema,
    status_code=status.HTTP_201_CREATED)
async def create_feedback(
        feedback_info: FeedbackInputSchema,
        session: AsyncSession = Depends(get_session),
) -> FeedbackSchema:
    return await FeedbackManager.create(
        session=session,
        input_data=feedback_info
    )


@feedback_router.patch(
    '/feedbacks/{feedback_id}',
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
    '/feedbacks/{feedback_id}',
    status_code=status.HTTP_204_NO_CONTENT)
async def delete_feedback(
        feedback_id: int,
        session: AsyncSession = Depends(get_session)
):
    await FeedbackManager.retrieve(id=feedback_id, session=session)
    return await FeedbackManager.delete(
        session=session,
        id=feedback_id
    )
