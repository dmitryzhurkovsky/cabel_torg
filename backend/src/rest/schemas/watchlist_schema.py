from pydantic import BaseModel

from src.rest.schemas.product_schema import ProductSchema


class WatchListInputSchema(BaseModel):
    product_id: int


class WatchListSchema(BaseModel):
    user_id: int
    product_id: int

    class Config:
        from_attributes = True


class WatchListWithProductSchema(BaseModel):
    product: ProductSchema

    class Config:
        from_attributes = True
