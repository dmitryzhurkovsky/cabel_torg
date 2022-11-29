from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.db.db import Base


class WatchList(Base):
    __tablename__ = 'watch_lists'

    product_id = Column(ForeignKey("products.id"), primary_key=True)
    product = relationship("Product", back_populates="added_to_watchlist_for")

    user_id = Column(ForeignKey("users.id"), primary_key=True)
    user = relationship("User", back_populates="products_in_watchlist")
