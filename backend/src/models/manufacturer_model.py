from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.models.abstract_model import Base1CModel


class Manufacturer(Base1CModel):
    __tablename__ = 'manufacturers'

    name = Column(String(255))

    products = relationship('Product', back_populates='manufacturer')

    def __str__(self):
        return self.name
