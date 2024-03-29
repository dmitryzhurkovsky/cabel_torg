from pydantic import BaseModel

from src.rest.schemas.product_schema import ProductSchema


class CartCreateInputSchema(BaseModel):
    product_id: int
    amount: int


class CartUpdateInputSchema(BaseModel):
    amount: int


class CartSchema(BaseModel):
    user_id: int
    product_id: int
    amount: int

    class Config:
        from_attributes = True


class CartWithProductSchema(BaseModel):
    amount: int
    product: ProductSchema

    class Config:
        from_attributes = True
