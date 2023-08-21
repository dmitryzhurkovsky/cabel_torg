from sqlalchemy import Column, Integer, DateTime, Boolean, Text
from sqlalchemy.sql.functions import now

from src.core.db.db import Base


class ParserInfo(Base):
    """
    It's used for getting actual information about parsing processes.
    """
    __tablename__ = 'service__parser_information'

    id = Column(Integer, index=True, primary_key=True)

    started_at = Column(DateTime, server_default=now())
    finished_at = Column(DateTime)
    files_were_updated_at = Column(DateTime)

    is_failed = Column(Boolean, default=False)

    exception = Column(Text)
