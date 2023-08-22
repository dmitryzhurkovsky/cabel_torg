from fastapi import APIRouter

from src.rest.api.v1.service_enitites.article_router import article_router
from src.rest.api.v1.service_enitites.delivery_type_router import delivery_type_router
from src.rest.api.v1.service_enitites.feedback_router import feedback_router
from src.rest.api.v1.service_enitites.partner_router import partner_router
from src.rest.api.v1.service_enitites.request_call_router import request_call_router
from src.rest.api.v1.service_enitites.vender_info_router import vendor_info_router
from src.rest.api.v1.service_enitites.banner_router import banner_router
from src.rest.api.v1.service_enitites.parser_router import parser_info_router

service_entities_router = APIRouter(prefix='/service_entities')
service_entities_router.include_router(article_router)
service_entities_router.include_router(delivery_type_router)
service_entities_router.include_router(partner_router)
service_entities_router.include_router(vendor_info_router)
service_entities_router.include_router(request_call_router)
service_entities_router.include_router(feedback_router)
service_entities_router.include_router(banner_router)
service_entities_router.include_router(parser_info_router)
