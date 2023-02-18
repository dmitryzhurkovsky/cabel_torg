import pathlib
from datetime import datetime

import jinja2
import pdfkit
from num2words import num2words
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import engine
from src.core.managers.order_manager import OrderManager
from src.models import Order, User
import locale


root_directory = pathlib.Path(__file__).parent.resolve()

template_loader = jinja2.FileSystemLoader(root_directory)
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('invoice_template.html')
styles = f'{root_directory}/style.css'
pdf_kit_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

# Set the locale to Russian
locale.setlocale(locale.LC_TIME, 'ru_RU')

final_price_text = num2words(325.5)


class InvoiceGenerator:
    """
    It's a service responsilbe for generating invoices.
    Data for an invoice is taken from an order - a datbase model.
    """

    __slots__ = ()

    @classmethod
    async def get_context(cls, order_id: int, user: User) -> dict:
        """Get context for for a jinja template."""
        async with AsyncSession(engine) as db:
            order: Order = await OrderManager.retrieve(id=order_id, session=db)

            return {
                'invoice_number': order.number,
                'created_at': datetime.now().strftime('%d от %B, %Y'),
                # 'month': month,
                # 'year': year,
                # 'customer_name': customer_name,
                'customer_requisites': cls.generate_customer_requirements(order),
                'contract_number': f'№ {order.number}',
                'final_price': 'cls.calculate_price'
            }

    @staticmethod
    def generate_customer_requirements(order: Order):
        return (
            f'{order.full_name}, {order.unp}, {order.legal_address}, '
            f'{order.IBAN} в банке {order.serving_bank}, {order.BIC}'
        )

    @classmethod
    def generate_invoice(cls, order_id: int) -> bytes:
        context = cls.get_context()
        payload = template.render(context)

        return pdfkit.PDFKit(
            url_or_file=payload,
            type_='string',
            configuration=pdf_kit_config,
            css=styles,
            options=options
        ).to_pdf()
