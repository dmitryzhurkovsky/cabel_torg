from sqlalchemy import Column, ForeignKey, Integer, CheckConstraint
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class Cart(Base):
    __tablename__ = 'carts'

    product_id = Column(ForeignKey("products.id"), primary_key=True)
    product = relationship("Product", back_populates="added_to_cart_for")

    user_id = Column(ForeignKey("users.id"), primary_key=True)
    user = relationship("User", back_populates="products_in_cart")

    amount = Column(Integer)

    __tableargs__ = (
        CheckConstraint(amount > 0, name='check_count_should_be_positive')
    )