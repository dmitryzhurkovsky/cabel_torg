from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql.functions import now, current_timestamp

from src.core.db.db import Base


class BaseModel(Base):
    """
    Base model for all models with id, created_at, updated_at fields
    """
    __abstract__ = True

    id = Column(Integer, index=True, primary_key=True)

    created_at = Column(DateTime, server_default=now())
    updated_at = Column(DateTime, server_default=now(), onupdate=current_timestamp())


class Base1CModel(BaseModel):
    """
    Base model for all entities from 1C bookkeeping with bookkeeping_id
    """
    __abstract__ = True

    bookkeeping_id = Column(String(128), unique=True)  # id from 1C
