import locale
import pathlib
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from sys import platform
from num2words import num2words

import jinja2
import pdfkit
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.core.db.db import engine
from src.rest.managers.order_manager import OrderManager
from src.models import Order

root_directory = pathlib.Path(__file__).parent.resolve()

if platform == 'darwin':  # OS X(Apple)
    wkhtmltopdf_executor = '/usr/local/bin/wkhtmltopdf'
else:
    wkhtmltopdf_executor = '/usr/bin/wkhtmltopdf'

template_loader = jinja2.FileSystemLoader(root_directory)
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('invoice_template.html')
styles = f'{root_directory}/style.css'
pdf_kit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_executor)
pdf_kit_options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    'enable-local-file-access': ''
}
# Set the locale to Russian
locale.setlocale(locale.LC_TIME, 'ru_RU')


@dataclass
class ProductJinjaSchema:
    name: str
    amount: int
    base_unit: str
    price: Decimal | float
    cost: Decimal | float
    tax: int
    tax_sum: Decimal | float
    price_with_tax: Decimal | float
    weight: Decimal | float | None

    # It's a special discount if a customer buys a lot of products a vendor can provide a special discount.
    price_with_tax_and_ordr_discount: Decimal | float


class InvoiceGenerator:
    """
    It's a service responsilbe for generating invoices.
    Data for an invoice is taken from an order - a datbase model.
    """

    __slots__ = ()

    @classmethod
    async def get_context(cls, order_id: int) -> dict:
        """Get context for for a jinja template."""
        async with AsyncSession(engine) as db:
            order: Order = await OrderManager.retrieve(id=order_id, session=db)

            order_products = []
            products_tax_sum = 0
            products_price_with_tax = 0

            for product in order.products:
                tax_sum = product.product.tax_sum * product.amount
                products_tax_sum += tax_sum

                price_with_tax = product.product.actual_price_with_tax * product.amount
                products_price_with_tax += price_with_tax

                order_products.append(ProductJinjaSchema(
                    name=product.product.name,
                    amount=product.amount,
                    weight=product.product.weight if product.product.weight else '',
                    base_unit=product.product.base_unit.full_name,
                    price=product.product.actual_price,
                    cost=product.amount * product.product.actual_price,
                    tax=product.product.tax,
                    tax_sum=round(tax_sum, 2),
                    price_with_tax=round(price_with_tax, 2),
                    price_with_tax_and_ordr_discount=round(
                        price_with_tax * order.discount if order.discount else price_with_tax, 2
                    ),
                ))

            return {
                'invoice_number': order.number,
                'created_at': datetime.now().strftime('%d %B, %Y'),
                'customer_requisites': cls.generate_customer_requirements(order),
                'contract_number': f'№ {order.number}',
                'products': order_products,
                'products_tax_sum': num2words(round(products_tax_sum, 2)),
                'products_price_with_tax': num2words(round(products_price_with_tax, 2)),

                'static_url': settings.STATIC_PATH
            }

    @staticmethod
    def generate_customer_requirements(order: Order) -> str:
        return (
            f'{order.full_name}, {order.unp}, {order.legal_address}, '
            f'{order.IBAN} в банке {order.serving_bank}, {order.BIC}'
        )

    @classmethod
    async def generate_invoice(cls, order_id: int) -> bytes:
        context = await cls.get_context(order_id=order_id)
        payload = template.render(context)

        return pdfkit.PDFKit(
            url_or_file=payload,
            type_='string',
            configuration=pdf_kit_config,
            css=styles,
            options=pdf_kit_options
        ).to_pdf()
