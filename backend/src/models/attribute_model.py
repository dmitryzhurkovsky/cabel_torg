from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.core.db.db import Base
from src.models.abstract_model import Base1CModel


class ProductAttribute(Base):
    __tablename__ = 'product_attribute'

    attribute_id = Column(ForeignKey("attributes.id", ondelete='CASCADE'), primary_key=True)
    product_id = Column(ForeignKey("products.id", ondelete='CASCADE'), primary_key=True)


class Attribute(Base):
    __tablename__ = 'attributes'

    id = Column(Integer, index=True, primary_key=True)

    value_id = Column(Integer, ForeignKey('attribute_values.id', ondelete='CASCADE'))
    value = relationship('AttributeValue', back_populates='attribute', lazy='joined')

    name_id = Column(Integer, ForeignKey('attribute_names.id', ondelete='CASCADE'))
    name = relationship('AttributeName', back_populates='attribute', lazy='joined')

    products = relationship('Product', secondary='product_attribute', back_populates='attributes', lazy='noload')

    def __str__(self):
        return self.value


class AttributeValue(Base1CModel):
    __tablename__ = 'attribute_values'

    payload = Column(String(255), nullable=False, unique=False)

    attribute = relationship('Attribute', back_populates='value', lazy='noload')


class AttributeName(Base1CModel):
    __tablename__ = 'attribute_names'

    payload = Column(String(255), nullable=False, unique=False)

    attribute = relationship('Attribute', back_populates='name', lazy='noload')
