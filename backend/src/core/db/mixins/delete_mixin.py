from typing import Any

from fastapi import HTTPException
from sqlalchemy import delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin
from src.core.enums import SessionStatusEnum


class DeleteMixin(BaseMixin):
    @classmethod
    async def delete(cls, session: AsyncSession, **kwargs: Any) -> dict | HTTPException:
        """Delete object by keys"""
        filtered_fields = cls.init_filtered_fields(filter_fields=kwargs)

        await session.execute(
            delete(cls.table).
            filter(and_(True, *filtered_fields))
        )
        await session.commit()

        return {'status': SessionStatusEnum.SUCCESS.value}

