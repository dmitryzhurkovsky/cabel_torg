from sqlalchemy import Column, Integer, String, Boolean

from src.models.abstract_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    full_name = Column(String, unique=True)
    phone_number = Column(String, unique=True)

    # requisites
    company_name = Column(String)
    unp = Column(String)  # Payer's Account Number
    legal_address = Column(String)
    IBAN = Column(String)
    BIC = Column(String)  # Belarusian Central Bank Identification Code
    serving_bank = Column(String)

    # service fields
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
