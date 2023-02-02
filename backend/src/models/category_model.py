from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    CheckConstraint
)
from sqlalchemy.orm import backref, relationship

from src.models.abstract_model import Base1CModel


class Category(Base1CModel):
    """It's a group in a 1C dump"""
    __tablename__ = 'categories'

    id = Column(Integer, index=True, primary_key=True)
    order = Column(Integer, nullable=True, unique=False)
    # An idea of ordering is:
    # an oder attribute of parent categories is 1000, 2000, 3000;
    # an oder attribute of subcategories is 1100, 1200, 1300
    # an oder attribute of subcategories' subcategories is 1101, 1102, 1103

    name = Column(String)

    products = relationship('Product', back_populates='category', lazy='noload')

    parent_category_id = Column(Integer, ForeignKey('categories.id'))
    subcategories = relationship(
        'Category',
        backref=backref('parent_category', remote_side=[id]),
        viewonly=True,
    )
    discount = Column(Integer, default=0)

    __tableargs__ = (
        CheckConstraint(discount < 100, name='check_discount_less_than_100'),
    )

    def __str__(self):
        return self.name
