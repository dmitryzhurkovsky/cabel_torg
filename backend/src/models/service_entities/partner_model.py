from sqlalchemy import Column, String, Integer

from src.core.db.db import Base


class Partner(Base):
    __tablename__ = 'partners'

    id = Column(Integer, index=True, primary_key=True)
    image = Column(String, nullable=True)
