from http.client import HTTPException
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin, TableType


class RetrieveMixin(BaseMixin):
    @classmethod
    async def retrieve(
            cls,
            session: AsyncSession,
            **kwargs: Any
    ) -> TableType | HTTPException:
        """
        Retrieve an object from the database based on the provided primary key or other fields.
        If use_or_conditions attribute is True, then it will combine filters by or_ operand.
        """
        filtered_fields = cls.init_filtered_fields(filter_fields=kwargs)

        query = await session.execute(
            select(cls.table).
            where(*filtered_fields).
            options(*cls.preloaded_fields)
        )
        obj = query.scalar_one_or_none()
        cls._check_object(obj=obj)

        return obj
