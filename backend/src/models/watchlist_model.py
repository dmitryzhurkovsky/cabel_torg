from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class WatchList(Base):
    """
    How to build a relation:
    Column(ForeignKey('table_name.id'), primary_key=True)
    relationship('ModelName', back_populates="field_name_in_linked_table)
    """
    __tablename__ = 'watch_lists'

    product_id = Column(ForeignKey('products.id'), primary_key=True)
    product = relationship('Product', back_populates='added_to_watchlist_for')

    user_id = Column(ForeignKey('users.id'), primary_key=True)
    user = relationship('User', back_populates='products_in_watchlist')
