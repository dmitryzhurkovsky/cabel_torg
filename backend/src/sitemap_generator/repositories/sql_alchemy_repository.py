from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import TableType
from src.sitemap_generator.query_contexts.sql_query_context import SQLAlchemyQueryContext
from src.sitemap_generator.repositories.abstract_repository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, table: TableType, db: AsyncSession):
        self.db = db
        self.table = table
        self._query_context = SQLAlchemyQueryContext(self.table)

    async def get_all_records(self):
        filter_expression = self.query_context.filter_expressions or tuple()
        select_fields = self.query_context.select_fields or [self.table]

        query_result = await self.db.execute(
            select(*select_fields).
            where(*filter_expression)
        )
        if self.query_context.select_fields:
            return query_result.all()

        return query_result.scalars().all()

    @property
    def query_context(self) -> SQLAlchemyQueryContext:
        return self._query_context

    @query_context.setter
    def query_context(self, v: SQLAlchemyQueryContext):
        self._query_context = v
