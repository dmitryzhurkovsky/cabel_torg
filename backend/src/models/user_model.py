from sqlalchemy import Column, String, Boolean, CheckConstraint
from sqlalchemy.orm import relationship

from src.models.abstract_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    full_name = Column(String(50), nullable=False)
    phone_number = Column(String(50), unique=True, nullable=False)

    # requisites
    company_name = Column(String(50), nullable=False)
    unp = Column(String(9), nullable=False)  # Payer's Account Number
    delivery_address = Column(String(128))
    legal_address = Column(String(128))
    IBAN = Column(String(34))
    BIC = Column(String(50))  # Belarusian Central Bank Identification Code
    serving_bank = Column(String(128))

    # service fields
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    products_in_cart = relationship('Cart', back_populates='user')
    products_in_watchlist = relationship('WatchList', back_populates='user')
    orders = relationship('Order', back_populates='user')

    __tableargs__ = (
        CheckConstraint('char_length(unp) = 9', name='check_length_of_unp_is_nine_symbols')
    )

    def __str__(self):
        return self.email
