from fastapi import APIRouter

from src.rest.api.v1.auth_router import auth_router
from src.rest.api.v1.cart_router import cart_router
from src.rest.api.v1.category_router import category_router
from src.rest.api.v1.product_router import product_router
from src.rest.api.v1.user_router import user_router
from src.rest.api.v1.watchlist_router import watchlist_router

api_v1 = APIRouter(prefix='/v1')

api_v1.include_router(category_router)
api_v1.include_router(product_router)
api_v1.include_router(auth_router)
api_v1.include_router(user_router)
api_v1.include_router(cart_router)
api_v1.include_router(watchlist_router)
