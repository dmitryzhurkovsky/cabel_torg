from sqlalchemy import Column, ForeignKey, Integer, CheckConstraint
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class Cart(Base):
    """
    How to build a relation:
    Column(ForeignKey('table_name.id'), primary_key=True)
    relationship('ModelName', back_populates="field_name_in_linked_table)
    """
    __tablename__ = 'carts'

    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    product = relationship('Product', back_populates='added_to_carts')

    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    user = relationship('User', back_populates='products_in_cart')

    amount = Column(Integer)

    __tableargs__ = (
        CheckConstraint(amount > 0, name='check_count_should_be_positive')
    )
