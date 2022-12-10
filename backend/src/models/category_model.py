from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from src.models.abstract_model import Base1CModel


class Category(Base1CModel):
    """It's a group in a 1C dump"""
    __tablename__ = 'categories'

    id = Column(Integer, index=True, primary_key=True)

    name = Column(String)

    products = relationship('Product', back_populates='category')

    parent_category_id = Column(Integer, ForeignKey('categories.id'))
    subcategories = relationship('Category', backref=backref('parent_category', remote_side=[id]))

    def __str__(self):
        return self.name
