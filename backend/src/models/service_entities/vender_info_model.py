from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class Address(Base):
    __tablename__ = 'service__addresses'

    id = Column(Integer, index=True, primary_key=True)

    title = Column(String(255))
    payload = Column(String)

    vendor_info_id = Column(Integer, ForeignKey('service__vendor_info.id'))  # o2m
    vendors = relationship('VendorInfo', back_populates='addresses', lazy='noload')


class VendorInfo(Base):
    """The model is responsible for data in footer and so on."""

    __tablename__ = 'service__vendor_info'

    id = Column(Integer, index=True, primary_key=True)

    phone = Column(String(255))
    email = Column(String(255))
    logo = Column(String(255))

    director_fullname = Column(String(255))

    unp = Column(String(9))  # Payer's Account Number
    OKPO = Column(String(10))
    legal_address = Column(String(256))
    postal_address = Column(String(256))
    phone_and_fax = Column(String(128))

    serving_bank = Column(String(128))
    serving_bank_short = Column(String(128))
    IBAN = Column(String(35))
    RUR = Column(String(35))

    # Social media
    instagram_url = Column(String)
    facebook_url = Column(String)
    vk_url = Column(String)
    telegram_url = Column(String)
    twitter_url = Column(String)
    tiktok_url = Column(String)
    youtube_url = Column(String)

    addresses = relationship('Address', back_populates='vendors', lazy='joined')
