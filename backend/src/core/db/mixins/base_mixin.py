from typing import TypeVar, Type

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import selectinload

from src.core.db.db import Base
from src.core.exception.base_exception import ObjectNotFoundError

TableType = TypeVar('TableType', bound=Base)
CreateBaseSchema = TypeVar('CreateBaseSchema', bound=BaseModel)
UpdateBaseSchema = TypeVar('UpdateBaseSchema', bound=BaseModel)


class BaseMixin:
    """Base async database mixin"""

    table: TableType = None
    create_scheme: CreateBaseSchema | None = None
    update_scheme: UpdateBaseSchema | None = None

    @classmethod
    def init_filtered_fields(cls, filter_fields: dict) -> list:
        """Initiate filter fields for query"""
        initiated_filter_fields = []

        for name, value in filter_fields.items():
            initiated_filter_fields.append(getattr(cls.table, name) == value)

        return initiated_filter_fields

    @classmethod
    def init_prefetch_related_fields(cls, prefetch_fields: tuple) -> tuple:
        """Initiate fields that will be loaded in query to database for related fields"""
        return (selectinload(field) for field in prefetch_fields) if prefetch_fields else tuple()

    @classmethod
    def _check_object(cls, obj: TableType) -> None | Type[HTTPException]:
        """Check if object exist"""
        if not obj:
            raise ObjectNotFoundError()
