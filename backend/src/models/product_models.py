import base64

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from src.models.abstract_model import Base1CModel


class Category(Base1CModel):
    __tablename__ = 'categories'

    id = Column(Integer, index=True, primary_key=True)

    name = Column(String)

    products = relationship('Product', back_populates='category')

    parent_category_id = Column(Integer, ForeignKey('categories.id'))
    subcategories = relationship('Category', backref=backref('parent_category', remote_side=[id]))


class Manufacturer(Base1CModel):
    __tablename__ = 'manufacturers'

    name = Column(String)

    products = relationship('Product', back_populates='manufacturer')


class Product(Base1CModel):
    __tablename__ = 'products'

    vendor_code = Column(String, nullable=True)
    name = Column(String)
    base_unit = Column(String)
    image_path = Column(String, nullable=True)
    tax = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)

    @property
    def image(self):
        if self.image_path:
            with open(f'src/static/{self.image_path}', 'rb') as image_file:  # todo set static path
                return base64.b64encode(image_file.read())

        return None

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    manufacturer = relationship('Manufacturer', back_populates='products')
