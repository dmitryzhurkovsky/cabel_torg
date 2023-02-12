from http.client import HTTPException
from typing import Any

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.db.mixins.base_mixin import BaseMixin, TableType


class RetrieveMixin(BaseMixin):
    @classmethod
    async def retrieve(
            cls,
            session: AsyncSession = Depends(get_session),
            **kwargs: Any
    ) -> TableType | HTTPException:
        """Get object by primary key or by another fields"""
        filtered_fields = cls.init_filtered_fields(filter_fields=kwargs)

        query = await session.execute(
            select(cls.table).
            where(*filtered_fields).
            options(*cls.preloaded_fields)
        )
        obj = query.scalar_one_or_none()
        cls._check_object(obj=obj)

        return obj
