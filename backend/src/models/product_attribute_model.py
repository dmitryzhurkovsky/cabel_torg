from sqlalchemy import Column, ForeignKey

from src.core.db.db import Base


class ProductAttribute(Base):
    __tablename__ = 'product_attribute'

    attribute_id = Column(ForeignKey("attributes.id"), primary_key=True)
    product_id = Column(ForeignKey("products.id"), primary_key=True)
