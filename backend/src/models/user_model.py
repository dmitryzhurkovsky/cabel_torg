from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from src.models.abstract_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String, unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    full_name = Column(String)
    phone_number = Column(String, unique=True)

    # requisites
    company_name = Column(String)
    unp = Column(String)  # Payer's Account Number
    delivery_address = Column(String)
    legal_address = Column(String)
    IBAN = Column(String)
    BIC = Column(String)  # Belarusian Central Bank Identification Code
    serving_bank = Column(String)

    # service fields
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    products_in_cart = relationship('Cart', back_populates='user')
    products_in_watchlist = relationship('WatchList', back_populates='user')
    orders = relationship('Order', back_populates='user')

    def __str__(self):
        return self.email
