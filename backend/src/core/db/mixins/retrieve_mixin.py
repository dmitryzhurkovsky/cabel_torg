from http.client import HTTPException
from typing import Any

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.core.db.db import get_session
from src.core.db.mixins.base_mixin import BaseMixin, TableType


class RetrieveMixin(BaseMixin):
    @classmethod
    async def retrieve(
            cls,
            session: AsyncSession = Depends(get_session),
            prefetch_fields: tuple = None,
            **kwargs: Any
    ) -> TableType | HTTPException:
        """Get list of objects"""
        key = [*kwargs][0]

        options = [selectinload(field) for field in prefetch_fields] if prefetch_fields else tuple

        result = await session.execute(
            select(cls.table).
            filter(getattr(cls.table, key) == kwargs.get(key)).
            options(*options)
        )
        obj = result.scalar_one_or_none()
        await session.refresh(obj)

        return obj
