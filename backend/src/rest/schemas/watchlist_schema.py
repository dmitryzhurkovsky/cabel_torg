from pydantic import BaseModel

from src.rest.schemas.product_schema import ProductInWatchListSchema


class WatchListInputSchema(BaseModel):
    product_id: int


class WatchListSchema(BaseModel):
    user_id: int
    product_id: int

    class Config:
        orm_mode = True


class WatchListWithProductSchema(BaseModel):
    product: ProductInWatchListSchema

    class Config:
        orm_mode = True
