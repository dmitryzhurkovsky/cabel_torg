from typing import TypeVar, Type

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import or_
from sqlalchemy.orm import selectinload

from src.core.db.db import Base
from src.core.exception.base_exception import ObjectNotFoundError

TableType = TypeVar('TableType', bound=Base)
CreateBaseSchema = TypeVar('CreateBaseSchema', bound=BaseModel)
UpdateBaseSchema = TypeVar('UpdateBaseSchema', bound=BaseModel)


class BaseMixin:
    """
    Base async database mixin.
    preloaded_fields are fields that should be fetched with query not to get I/O error.
    base_filters are filters that should be forced to apply to each get query.
    """
    table: TableType = None
    preloaded_fields: tuple = ()
    base_filters: tuple = ()

    create_scheme: CreateBaseSchema | None = None
    update_scheme: UpdateBaseSchema | None = None

    @classmethod
    def init_filtered_fields(cls, filter_fields: dict) -> list:
        """Initiate filter fields for a query."""
        initiated_filter_fields = []
        use_or_conditions = filter_fields.pop('use_or_condition', False)

        for name, value in filter_fields.items():
            model_attribute = getattr(cls.table, name)
            if model_attribute.type.python_type == type(value):  # To escape situations when we try to filter integer firld by string.
                initiated_filter_fields.append(model_attribute == value)

        if use_or_conditions:
            initiated_filter_fields = (or_(*initiated_filter_fields),)
        return initiated_filter_fields

    @classmethod
    def init_m2m_filtered_fields(cls, filter_fields: dict) -> list:
        """Initiate filter fields for a query."""
        initiated_filter_fields = []

        for name, value in filter_fields.items():
            if 'id' in name:
                initiated_filter_fields.append(getattr(cls.table, name) == value)

        return initiated_filter_fields

    @classmethod
    def init_preloaded_fields(cls, preloaded_fields: tuple) -> tuple:
        """Initiate fields that will be preloaded in a query to database for related fields"""
        return (selectinload(field) for field in preloaded_fields) if preloaded_fields else tuple()

    @classmethod
    def _check_object(cls, obj: TableType) -> Type[HTTPException]:  # noqa
        """Check if object exist"""
        if not obj:
            raise ObjectNotFoundError()
