from fastapi import APIRouter, Response

from src.invoice_generator.main import InvoiceGenerator

invoice_router = APIRouter(tags=['orders'], prefix='/orders')


@invoice_router.post(
    '/{order_id}/invoices',
    response_class=Response
)
# todo add is_owner or is_admin or think about this
async def generate_invoice(
        order_id: int,
):
    invoice: bytes = await InvoiceGenerator.generate_invoice(order_id=order_id)
    return Response(invoice, media_type='application/pdf')
