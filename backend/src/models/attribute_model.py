from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.models.abstract_model import Base1CModel


class Attribute(Base1CModel):
    __tablename__ = 'attributes'

    value = Column(String(255), nullable=False, unique=True)

    products = relationship('Product', secondary='product_attribute', back_populates='attributes')

    def __str__(self):
        return self.value
