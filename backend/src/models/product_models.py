from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from src.core.db.db import Base


class BaseModel(Base):
    __abstract__ = True

    bookkeeping_id = Column(String(128), unique=True)  # id from !C


class Category(BaseModel):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    products = relationship('Product', back_populates='category')

    parent_category_id = Column(Integer, ForeignKey('categories.id'))
    subcategories = relationship('Category', backref=backref('parent_category', remote_side=[id]))


class Manufacturer(BaseModel):
    __tablename__ = 'manufacturers'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    products = relationship('Product', back_populates='manufacturer')


class Product(BaseModel):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)

    vendor_code = Column(String, nullable=True)
    name = Column(String)
    base_unit = Column(String)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')

    image = Column(String, nullable=True)

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    manufacturer = relationship('Manufacturer', back_populates='products')

    tax = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
