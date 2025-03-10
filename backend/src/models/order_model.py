from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    CheckConstraint,
    String,
    Enum
)
from sqlalchemy.orm import relationship

from src.core.db.db import Base
from src.core.enums import BaseEnum
from src.models.abstract_model import BaseModel


class OrderStatus(str, BaseEnum):
    IN_PROCESSING = 'P'
    SENT = 'S'
    CANCELED = 'c'
    COMPLETED = 'C'


class Order(BaseModel):
    __tablename__ = 'orders'

    status = Column('status', Enum(*OrderStatus.values(), name='order_status'), default=OrderStatus.IN_PROCESSING)
    promo_code = Column(String(50))

    # It's a special discount if a customer buys a lot of products a vendor can provide a special discount.
    # We can see it in an invoice.
    discount = Column(Integer, default=0)

    # requisites
    company_name = Column(String(50))
    unp = Column(String(9))  # Payer's Account Number
    legal_address = Column(String(128))
    IBAN = Column(String(35))
    BIC = Column(String(50))  # Belarusian Central Bank Identification Code
    serving_bank = Column(String(128))

    # contact information
    full_name = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(128))

    # delivery information
    city = Column(String(50))
    street = Column(String(128))
    house = Column(String(12))
    flat = Column(String(12))
    delivery_type = relationship('DeliveryType', back_populates='orders', lazy='joined')
    delivery_type_id = Column(ForeignKey('service__delivery_types.id'))

    # relations
    products = relationship('ProductOrder', back_populates='order', lazy='joined')

    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), index=True)
    user = relationship('User', back_populates='orders')

    @property
    def number(self) -> int:
        return self.id + 100000

    @property
    def total_price(self):
        return sum([product.amount * product.product.actual_price_with_tax() for product in self.products])


class ProductOrder(Base):
    __tablename__ = 'product_order'

    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    product = relationship('Product', back_populates='added_to_orders', lazy='joined')

    order_id = Column(ForeignKey('orders.id', ondelete='CASCADE'), primary_key=True)
    order = relationship('Order', back_populates='products')

    amount = Column(Integer)

    __tableargs__ = (
        CheckConstraint(amount > 0, name='check_count_should_be_positive')
    )
