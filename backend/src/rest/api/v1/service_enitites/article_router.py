from fastapi import APIRouter, Depends, status, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.managers.services_managers import ArticleManager
from src.rest.schemas.service_entities.article_schema import ArticleSchema, ArticleInputSchema

article_router = APIRouter(tags=['articles'])


@article_router.get('/articles', response_model=list[ArticleSchema])
async def get_articles(session: AsyncSession = Depends(get_session)) -> list[ArticleSchema]:
    return await ArticleManager.list(session=session)


@article_router.post('/articles', response_model=ArticleSchema, status_code=status.HTTP_201_CREATED)
async def create_article(
        article_info: ArticleInputSchema,
        session: AsyncSession = Depends(get_session),
) -> ArticleSchema:
    return await ArticleManager.create(
        session=session,
        input_data=article_info
    )


@article_router.post(
    '/articles/{article_id}/images',
    response_model=ArticleSchema,
    status_code=status.HTTP_201_CREATED)
async def upload_image_for_article(
        article_id: int,
        file: UploadFile,
        session: AsyncSession = Depends(get_session),
) -> ArticleSchema:
    article = await ArticleManager.retrieve(id=article_id, session=session)
    file_name = await ArticleManager.upload_file(pk=article_id, input_file=file)
    await ArticleManager.update(
        input_data={'image': file_name},
        pk=article_id,
        session=session
    )
    await session.refresh(article)

    return article


@article_router.patch('/articles/{article_id}', response_model=ArticleSchema)
async def update_info_about_article(
        article_id: int,
        article_info: ArticleInputSchema,
        session: AsyncSession = Depends(get_session)
) -> ArticleSchema:
    return await ArticleManager.update(
        session=session, pk=article_id, input_data=article_info.dict(exclude_unset=True)
    )


@article_router.delete('/articles/{article_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
        article_id: int,
        session: AsyncSession = Depends(get_session)
):
    article = await ArticleManager.retrieve(id=article_id, session=session)
    result = await ArticleManager.delete(
        id=article_id,
        session=session
    )
    ArticleManager.delete_file(file_name=article.image)

    return result
