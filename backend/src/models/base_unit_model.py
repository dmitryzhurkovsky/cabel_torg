from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class BaseUnit(Base):
    __tablename__ = 'base_units'

    id = Column(Integer, index=True, primary_key=True)

    code = Column(String(10), nullable=True)
    full_name = Column(String(50), nullable=True)
    international_abbreviated = Column(String(10), nullable=True)

    products = relationship('Product', back_populates='base_unit')

    def __str__(self):
        return self.vendor_code if self.vendor_code else self.full_name
