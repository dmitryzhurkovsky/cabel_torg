from sqlalchemy import Column, ForeignKey, Integer, CheckConstraint, String
from sqlalchemy.orm import relationship

from src.core.db.db import Base
from src.models.abstract_model import BaseModel


class Order(BaseModel):
    __tablename__ = 'orders'

    promo_code = Column(String(50), nullable=True)

    # requisites
    company_name = Column(String(50))
    unp = Column(String(9))  # Payer's Account Number
    legal_address = Column(String(128))
    IBAN = Column(String(34))
    BIC = Column(String(50))  # Belarusian Central Bank Identification Code
    serving_bank = Column(String(128))

    # contact information
    full_name = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(128))

    # delivery
    city = Column(String(50))
    address = Column(String(128))
    house = Column(String(12))
    flat = Column(String(12))
    delivery_type = relationship('DeliveryType', back_populates='orders')
    delivery_type_id = Column(ForeignKey('delivery_types.id'))

    # relations
    products = relationship('ProductOrder', back_populates='order')

    user_id = Column(ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')


class ProductOrder(Base):
    __tablename__ = 'product_orders'

    product_id = Column(ForeignKey('products.id'), primary_key=True)
    product = relationship('Product', back_populates='added_to_orders')

    order_id = Column(ForeignKey('orders.id'))
    order = relationship('Order', back_populates='products')

    amount = Column(Integer)

    __tableargs__ = (
        CheckConstraint(amount > 0, name='check_count_should_be_positive')
    )