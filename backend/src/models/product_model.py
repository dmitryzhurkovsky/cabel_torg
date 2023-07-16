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
    vendor_code = Column(String, nullable=False)  # It's a slug field.
    vendor_code_ru = Column(String)
    name = Column(String)
    images = Column(String)  # pictures paths in the following format: picture_1,picture_2,picture_3...
    tax = Column(Integer)  # todo delete or change it, because tax is always 20
    description = Column(String)
    count = Column(DECIMAL, default=0)
    weight = Column(DECIMAL, default=0)
    is_new = Column(Boolean, default=False)
    document_url = Column(String)

    # Price fields
    price = Column(DECIMAL)  # The attribute got from 1C bookkeeping.
    price_with_discount = Column(DECIMAL)  # This attribute is auto-calculated if we change the discount.
    discount = Column(Integer, default=0)
    is_price_on_request = Column(Boolean, default=False)

    # Service fields
    is_visible = Column(Boolean, default=True, nullable=False)
    site_link = Column(String)
    site_page_title = Column(String)
    site_page_description = Column(String)

    # Relationship fields
    attributes = relationship(
        'Attribute',
        secondary='product_attribute',
        back_populates='products',
        lazy='joined',
        order_by='Attribute.name_id'
    )  # m2m
    base_unit_id = Column(Integer, ForeignKey('base_units.id'))  # o2m
    base_unit = relationship('BaseUnit', back_populates='products', lazy='joined')
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'))  # o2m
    category = relationship('Category', back_populates='products', lazy='joined')
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))  # o2m
    manufacturer = relationship('Manufacturer', back_populates='products', lazy='joined')
    added_to_carts = relationship('Cart', back_populates='product', lazy='noload')  # m2m
    added_to_watchlist_for = relationship('WatchList', back_populates='product', lazy='noload')
    added_to_orders = relationship('ProductOrder', back_populates='product', lazy='noload')
    request_calls = relationship(
        'RequestCall',
        back_populates='product',
        lazy='noload',
        cascade="all, delete",
        passive_deletes=True
    )

# -------------------------------------- Admin panel's prices ----------------------------------------------------------
    @property
    def actual_discount(self) -> float | int | DECIMAL:
        """
        We have the following hierarchy of discounts:
        Product's discount -> Subcategory's discount -> Category discount.
        To set up a discount and support the hierarchy, we change the price only when calculating a discount
        for categories, and we change the discount field only when setting up the product's discount implicitly.

        It's used for:
        1. In the admin panel;
        2. calculating actual discount with tax.
        """
        if self.price_with_discount_and_tax and self.price_with_tax:
            return round(
                (self.price_with_tax - self.price_with_discount_and_tax)
                / self.price_with_tax * 100, 2
            )
        return 0

# -------------------------------------- Response model's prices -------------------------------------------------------
    @property
    def price_with_tax(self) -> float:
        """
        It's used for:
        1. As a field of the response schema;
        """
        if self.price:
            return round(self.price + (self.price * tax / 100), 2)

    @property
    def price_with_discount_and_tax(self) -> float | None:
        """
        It's used for:
        1. As a field of the response schema;
        """
        if self.price_with_discount:
            return round(self.price_with_discount + (self.price_with_discount * tax / 100), 2)

    @property
    def is_popular(self) -> bool:
        """
        It's used when we receive products in the following format:
        (Product_1, is_popular_1),
        (Product_2, is_popular_2),
        where Product is an instance of the product and is_popular is a value calculated as a subquery.
        We then set up the is_popular attribute for each product.
        """
        return self._is_popular

    @is_popular.setter
    def is_popular(self, value):
        """
        Check the documentation for the is_popular property.
        """
        self._is_popular = value

# -------------------------------------- Invoice generator's prices ----------------------------------------------------
    @property
    def tax_sum(self) -> float:
        """
        It's used for:
        1. Generating an invoice;
        2. Calculating actual discount with the tax.
        """
        return self.actual_price * tax / 100

    def actual_price_with_tax(self) -> float:
        """
        It's used for:
        1. generating an invoice;
        2. calculating the actual discount.
        """
        return self.tax_sum + self.actual_price

# -------------------------------------- Service prices ----------------------------------------------------------------
    @hybrid_property
    def actual_price(self) -> float:
        """
        This field is needed because we can have prices where a tax isn't set, but we still want to show users products
        with both a discount and without a discount.
        For example, we should show products with a price ranging from 10 to 20.
        If we filter only by the usual price, we may encounter a situation
        where a product has a price of 23 with a discount of 15,
        but it isn't shown because we are filtering only by the usual price.

        This field doesn't return back to the frontend. It is a service field.

        It's used for:
        1. Calculating the actual price with tax;
        2. Generating an invoice;
        3. Ordering and sorting on the backend.
        """
        return self.price_with_discount if self.price_with_discount else self.price

    @actual_price.expression
    def actual_price(cls):
        """It's expression for actual price."""
        return case(
            (Product.price_with_discount > 0, Product.price_with_discount),
            else_=Product.price
        )

# ----------------------------------------------------------------------------------------------------------------------

    __tableargs__ = (
        CheckConstraint(discount < 100, name='check_discount_lt_100'),
        CheckConstraint(discount >= 0, name='check_discount_gte_0'),
    )
