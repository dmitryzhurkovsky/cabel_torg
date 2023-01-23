from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.core import settings
from src.core.db.db import Base
from src.models.abstract_model import BaseModel


class Article(BaseModel):
    __tablename__ = 'articles'

    title = Column(String)
    text = Column(String, nullable=True)
    images = Column(String, nullable=True)

    @property
    def preview_text(self) -> str:
        return self.text[:settings.PREVIEW_TEXT_LENGTH] if self.text else ''


class Partner(Base):
    __tablename__ = 'partners'

    id = Column(Integer, index=True, primary_key=True)
    image = Column(String, nullable=True)


class DeliveryType(Base):
    __tablename__ = 'delivery_types'
    id = Column(Integer, index=True, primary_key=True)

    payload = Column(String(50))
    orders = relationship('Order', back_populates='delivery_type')
