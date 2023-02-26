from sqlalchemy import ColumnOperators
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import QueryParams

from src.core.db.mixins.upload_file_mixin import FileMixin
from src.rest.managers.base_manager import CRUDManager
from src.models.service_entities import *


class ArticleManager(CRUDManager, FileMixin):
    table = Article


class DeliveryTypeManager(CRUDManager):
    table = DeliveryType


class PartnerManager(CRUDManager, FileMixin):
    table = Partner


class AddressManager(CRUDManager):
    table = Address


class VendorInfoManager(CRUDManager):
    table = VendorInfo


class RequestCallManager(CRUDManager):
    table = RequestCall

    @staticmethod
    def get_filter_expressions(filter_fields: QueryParams) -> list[ColumnOperators | None]:
        if type_of_request_call := filter_fields.get('type_of_request_call'):
            if type_of_request_call == RequestCallType.GOOD_RECEIPT:
                return [RequestCall.type == RequestCallType.GOOD_RECEIPT.value, ]

        return []

    @classmethod
    async def filter_list(
            cls,
            filters: QueryParams,
            session: AsyncSession,
            custom_preloaded_fields: tuple | list = (),
            offset: int = 0,
            limit: int = 100
    ) -> list:
        """Get filtered list of objects with pagination."""
        filter_expressions = cls.get_filter_expressions(filters)

        return await cls.list(
            where=filter_expressions,
            session=session,
            custom_preloaded_fields=custom_preloaded_fields,
            offset=offset,
            limit=limit
        )


class FeedbackManager(CRUDManager):
    table = Feedback
