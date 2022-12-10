from pydantic import BaseModel


class ProductInWatchListInputSchema(BaseModel):
    product_id: int


class ProductInWatchListSchema(BaseModel):
    user_id: int
    product_id: int

    class Config:
        orm_mode = True
