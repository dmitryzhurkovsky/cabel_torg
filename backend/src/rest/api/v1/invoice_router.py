from fastapi import APIRouter, Response, Depends

from src.invoice_generator.main import InvoiceGenerator
from src.services.auth_service import AuthService

invoice_router = APIRouter(tags=['orders'])


@invoice_router.post('/orders/{order_id}/invoices', response_class=Response)
async def generate_invoice(
    order_id: int,
    user=Depends(AuthService.get_current_user),
):
    invoice: bytes = await InvoiceGenerator.generate_invoice(order_id=order_id)
    return Response(invoice, media_type='application/pdf')