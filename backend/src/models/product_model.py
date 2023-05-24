from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    CheckConstraint,
    Boolean,
    Enum,
    case,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from src.core import settings
from src.core.enums import BaseEnum
from src.models.abstract_model import Base1CModel

tax = settings.DEFAULT_TAX


class ProductStatus(str, BaseEnum):
    AVAILABLE = 'A'
    ON_THE_WAY_TO_THE_WAREHOUSE = 'W'
    OUT_OF_STOCK = 'O'


class Product(Base1CModel):
    __tablename__ = 'products'

    status = Column('status', Enum(*ProductStatus.values(), name='product_status'))
    vendor_code = Column(String)
    name = Column(String)
    images = Column(String)  # pictures paths in the following format: picture_1,picture_2,picture_3...
    tax = Column(Integer)  # todo change it, because tax is always 20
    description = Column(String)
    count = Column(DECIMAL, default=0)
    weight = Column(DECIMAL, default=0)
    is_new = Column(Boolean, default=False)

    # Price fields
    price = Column(DECIMAL)
    price_with_discount = Column(DECIMAL)  # This attribute is auto-calculated if we change the discount.
    discount = Column(Integer, default=0)

    # Service fields
    is_visible = Column(Boolean, default=True)
    site_link = Column(String)
    site_page_title = Column(String)
    site_page_description = Column(String)

    # Relationship fields
    attributes = relationship(
        'Attribute',
        secondary='product_attribute',
        back_populates='products',
        lazy='joined'
    )  # m2m

    base_unit_id = Column(Integer, ForeignKey('base_units.id'))  # o2m
    base_unit = relationship('BaseUnit', back_populates='products', lazy='joined')

    category_id = Column(Integer, ForeignKey('categories.id'))  # o2m
    category = relationship('Category', back_populates='products', lazy='joined')

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))  # o2m
    manufacturer = relationship('Manufacturer', back_populates='products', lazy='joined')

    added_to_carts = relationship('Cart', back_populates='product', lazy='noload')  # m2m

    added_to_watchlist_for = relationship('WatchList', back_populates='product', lazy='noload')

    added_to_orders = relationship('ProductOrder', back_populates='product', lazy='noload')

    request_calls = relationship('RequestCall', back_populates='product', lazy='noload')

    __tableargs__ = (
        CheckConstraint(discount < 100, name='check_discount_lt_100'),
        CheckConstraint(discount >= 0, name='check_discount_gte_0'),
    )

    @property
    def actual_discount(self) -> float | int | DECIMAL:
        """
        It's an actulal dsicount. It's used for admin panel.
        Since we calculate price depending on discount in cateogries and products and
        in its case we change only price.
        """
        if self.price_with_discount_and_tax:
            return round(
                (self.price_with_tax - self.price_with_discount_and_tax)
                / self.price_with_tax * 100, 2
            )
        return 0

    @property
    def price_with_tax(self) -> float:
        if self.price:
            return round(self.price + (self.price * tax / 100), 2)

    @property
    def price_with_discount_and_tax(self) -> float | None:
        if self.price_with_discount:
            return round(self.price_with_discount + (self.price_with_discount * tax / 100), 2)

    @property
    def tax_sum(self) -> float:
        """For generating an invoice."""
        return self.actual_price * tax / 100

    @hybrid_property
    def actual_price(self) -> float:
        """For generating an invoice, ordering and sorting."""
        return self.price_with_discount if self.price_with_discount else self.price

    @actual_price.expression
    def actual_price(cls):
        """For generating an invoice, ordering and sorting."""
        return case(
            (Product.price_with_discount > 0, Product.price_with_discount),
            else_=Product.price
        )

    def actual_price_with_tax(self) -> float:
        """For generating an invoice."""
        return self.tax_sum + self.actual_price
