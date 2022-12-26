from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.models.abstract_model import Base1CModel
from src.core.db.db import Base


class Attribute(Base):
    __tablename__ = 'attributes'

    id = Column(Integer, index=True, primary_key=True)

    value_id = Column(Integer, ForeignKey('attribute_values.id'))
    value = relationship('AttributeValue', back_populates='attribute')

    name_id = Column(Integer, ForeignKey('attribute_names.id'))
    name = relationship('AttributeName', back_populates='attribute')

    products = relationship('Product', secondary='product_attribute', back_populates='attributes')

    def __str__(self):
        return self.value


class AttributeValue(Base1CModel):
    __tablename__ = 'attribute_values'

    payload = Column(String(255), nullable=False, unique=False)

    attribute = relationship('Attribute', back_populates='value')


class AttributeName(Base1CModel):
    __tablename__ = 'attribute_names'

    payload = Column(String(255), nullable=False, unique=False)

    attribute = relationship('Attribute', back_populates='name')
