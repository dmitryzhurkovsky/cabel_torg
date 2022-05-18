from fastapi import APIRouter

from src.rest.api.v1.category import categories_router
from src.rest.api.v1.product import product_router

api_v1 = APIRouter(prefix='/v1')

api_v1.include_router(categories_router)
api_v1.include_router(product_router)
