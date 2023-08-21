from typing import Any, Sequence

from sqlalchemy import ColumnOperators, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette.datastructures import QueryParams

from src.core.db.mixins.upload_file_mixin import FileMixin
from src.models.service_entities import *
from src.rest.managers.base_manager import CRUDManager


class ArticleManager(CRUDManager, FileMixin):
    table = Article


class DeliveryTypeManager(CRUDManager):
    table = DeliveryType


class PartnerManager(CRUDManager, FileMixin):
    table = Partner


class AddressManager(CRUDManager):
    table = Address


class FeedbackManager(CRUDManager):
    table = Feedback


class BannerManager(CRUDManager, FileMixin):
    table = Banner


class ParserInfoManager(CRUDManager):
    table = ParserInfo


class VendorInfoManager(CRUDManager, FileMixin):
    table = VendorInfo

    preloaded_fields = (
        selectinload(VendorInfo.addresses),
    )


class RequestCallManager(CRUDManager):
    table = RequestCall

    preloaded_fields = (
        selectinload(RequestCall.product),
    )

    @staticmethod
    def get_filter_expressions(filter_fields: QueryParams) -> list[ColumnOperators | None]:
        if type_of_request_call := filter_fields.get('type_of_request_call'):
            if type_of_request_call == RequestCallType.GOODS_RECEIPT:
                return [RequestCall.type == RequestCallType.GOODS_RECEIPT.value, ]

        return []

    @classmethod
    async def filter_list(
            cls,
            filters: QueryParams,
            session: AsyncSession,
            custom_preloaded_fields: tuple | list = (),
            offset: int = 0,
            limit: int = 100
    ) -> Sequence[Row | RowMapping | Any] | list:
        """Get filtered list of objects with pagination."""
        filter_expressions = cls.get_filter_expressions(filters)

        return await cls.list(
            where=filter_expressions,
            session=session,
            custom_preloaded_fields=custom_preloaded_fields,
            offset=offset,
            limit=limit
        )
