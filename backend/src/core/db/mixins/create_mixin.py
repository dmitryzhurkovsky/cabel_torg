from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin, TableType, CreateBaseSchema


class CreateMixin(BaseMixin):
    @classmethod
    async def create(
            cls,
            input_data: CreateBaseSchema,
            session: AsyncSession,
    ) -> TableType:
        """Create model"""
        obj = cls.table(
            **(input_data if isinstance(input_data, dict) else input_data.__dict__)
        )
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj
