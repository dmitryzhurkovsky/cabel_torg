from src.core.db.mixins.base_mixin import TableType
from src.sitemap_generator.query_contexts.base_query_context import AbstractQueryContext


class SQLAlchemyQueryContext(AbstractQueryContext):
    def __init__(self, table: TableType):
        self.table = table

        self._filter_expressions = None
        self._select_fields = None

    @property
    def filter_expressions(self) -> tuple:
        return self._filter_expressions

    @filter_expressions.setter
    def filter_expressions(self, v: tuple) -> None:
        self._filter_expressions = v

    @property
    def select_fields(self) -> tuple:
        return self._select_fields

    @select_fields.setter
    def select_fields(self, v: tuple) -> None:
        self._select_fields = v
