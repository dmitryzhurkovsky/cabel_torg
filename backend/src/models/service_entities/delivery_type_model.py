from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class DeliveryType(Base):
    __tablename__ = 'delivery_types'

    id = Column(Integer, index=True, primary_key=True)

    payload = Column(String(50))
    orders = relationship('Order', back_populates='delivery_type', lazy='noload')
