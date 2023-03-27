from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class DeliveryType(Base):
    __tablename__ = 'service__delivery_types'

    id = Column(Integer, index=True, primary_key=True)

    payload = Column(String(255))
    is_pickup = Column(Boolean, default=False)

    orders = relationship('Order', back_populates='delivery_type', lazy='noload')
