from fastapi import APIRouter, Depends, status, UploadFile, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.rest.managers.services_managers import BannerManager
from src.rest.permissions import is_admin_permission
from src.rest.schemas.service_entities.banner_schema import BannerSchema, BannerInputSchema

banner_router = APIRouter(tags=['banners'], prefix='/banners')


@banner_router.get('', response_model=list[BannerSchema])
async def get_banners(
        is_active: bool = Query(default=True),
        session: AsyncSession = Depends(get_session)
) -> list[BannerSchema]:
    return await BannerManager.list(
        session=session,
        where=(BannerManager.table.is_active == is_active,)
    )


@banner_router.get('/{banners_id}', response_model=BannerSchema)
async def get_banners(
        banners_id: int,
        session: AsyncSession = Depends(get_session)
) -> BannerSchema:
    return await BannerManager.retrieve(id=banners_id, session=session)


@banner_router.post(
    '',
    response_model=BannerSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(is_admin_permission)]
)
async def create_banner(
        banner_info: BannerInputSchema,
        session: AsyncSession = Depends(get_session),
) -> BannerSchema:
    return await BannerManager.create(
        session=session,
        input_data=banner_info
    )


@banner_router.post(
    '/{banner_id}/images',
    response_model=BannerSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(is_admin_permission)]
)
async def upload_image_for_banner(
        banner_id: int,
        file: UploadFile,
        session: AsyncSession = Depends(get_session),
) -> BannerSchema:
    banner = await BannerManager.retrieve(id=banner_id, session=session)
    file_name = await BannerManager.upload_file(pk=banner_id, input_file=file)
    await BannerManager.update(
        input_data={'image': file_name},
        pk=banner_id,
        session=session
    )
    await session.refresh(banner)

    return banner


@banner_router.patch(
    '/{banner_id}',
    response_model=BannerSchema,
    dependencies=[Depends(is_admin_permission)]
)
async def update_info_about_banner(
        banner_id: int,
        banner_info: BannerInputSchema,
        session: AsyncSession = Depends(get_session)
) -> BannerSchema:
    return await BannerManager.update(
        session=session, pk=banner_id, input_data=banner_info.dict(exclude_unset=True)
    )


@banner_router.delete(
    '/{banner_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(is_admin_permission)]
)
async def delete_banner(
        banner_id: int,
        session: AsyncSession = Depends(get_session)
):
    banner = await BannerManager.retrieve(id=banner_id, session=session)
    result = await BannerManager.delete(
        id=banner_id,
        session=session
    )
    BannerManager.delete_file(file_name=banner.image)

    return result
