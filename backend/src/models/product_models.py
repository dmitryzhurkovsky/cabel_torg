from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, CheckConstraint
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.orm import relationship

from src.core.enums import ProductType
from src.models.abstract_model import Base1CModel


class Product(Base1CModel):
    __tablename__ = 'products'

    vendor_code = Column(String)
    name = Column(String)
    images = Column(String)  # pictures paths in the following format: picture_1,picture_2,picture_3...
    tax = Column(Integer)
    description = Column(String)
    type = Column('type', pgEnum(ProductType.values(), name='type'))

    price = Column(DECIMAL)
    price_with_discount = Column(DECIMAL)  # This attribute is auto-calculated if we change the discount.
    discount = Column(Integer)

    attributes = relationship(
        'Attribute',
        secondary='product_attribute',
        back_populates='products',
    )  # m2m

    base_unit_id = Column(Integer, ForeignKey('base_units.id'))  # o2m
    base_unit = relationship('BaseUnit', back_populates='products', lazy='joined')

    category_id = Column(Integer, ForeignKey('categories.id'))  # o2m
    category = relationship('Category', back_populates='products', lazy='joined')

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))  # o2m
    manufacturer = relationship('Manufacturer', back_populates='products', lazy='joined')

    added_to_carts = relationship('Cart', back_populates='product', lazy='noload')  # m2m

    added_to_watchlist_for = relationship('WatchList', back_populates='product', lazy='noload')

    added_to_orders = relationship('ProductOrder', back_populates='product', lazy='noload')

    __tableargs__ = (
        CheckConstraint(discount < 100, name='check_discount_lt_100'),
        CheckConstraint(discount >= 0, name='check_discount_gte_0'),
    )
