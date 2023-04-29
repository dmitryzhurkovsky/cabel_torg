from fastapi import APIRouter, Response, Depends
from starlette.requests import Request

from src.invoice_generator.main import InvoiceGenerator
from src.rest.managers.order_manager import OrderManager
from src.rest.permissions import is_authenticated_permission

invoice_router = APIRouter(tags=['orders'], prefix='/orders')


@invoice_router.post(
    '/{order_id}/invoices',
    response_class=Response,
    dependencies=[Depends(is_authenticated_permission)],
)
async def generate_invoice(
        request: Request,
        order_id: int,
):
    await OrderManager.check_object_permission(request=request)
    invoice: bytes = await InvoiceGenerator.generate_invoice(order_id=order_id)
    return Response(invoice, media_type='application/pdf')
