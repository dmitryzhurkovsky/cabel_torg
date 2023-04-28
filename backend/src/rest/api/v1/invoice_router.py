from fastapi import APIRouter, Response, Depends

from src.invoice_generator.main import InvoiceGenerator
from src.rest.permissions import is_authenticated_permissions

invoice_router = APIRouter(tags=['orders'], prefix='/orders')


@invoice_router.post(
    '/{order_id}/invoices',
    response_class=Response,
    dependencies=[Depends(is_authenticated_permissions)]
)
# todo add is_owner or is_admin or think about this
async def generate_invoice(
        order_id: int,
):
    invoice: bytes = await InvoiceGenerator.generate_invoice(order_id=order_id)
    return Response(invoice, media_type='application/pdf')
