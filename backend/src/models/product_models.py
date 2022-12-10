from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.abstract_model import Base1CModel


class Product(Base1CModel):
    __tablename__ = 'products'

    vendor_code = Column(String, nullable=True)
    name = Column(String)
    image_path = Column(String, nullable=True)
    tax = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)

    attributes = relationship('Attribute', secondary='product_attribute', back_populates='products')  # m2m

    base_unit_id = Column(Integer, ForeignKey('base_units.id'))  # o2m
    base_unit = relationship('BaseUnit', back_populates='products')

    category_id = Column(Integer, ForeignKey('categories.id'))  # o2m
    category = relationship('Category', back_populates='products')

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))  # o2m
    manufacturer = relationship('Manufacturer', back_populates='products')

    added_to_carts = relationship('Cart', back_populates='product')  # m2m

    added_to_watchlist_for = relationship('WatchList', back_populates='product')

    def __str__(self):
        return self.name
