from pydantic import BaseModel


class ProductInCartInputSchema(BaseModel):
    product_id: int
    amount: int


class ProductInCartSchema(BaseModel):
    user_id: int
    product_id: int
    amount: int

    class Config:
        orm_mode = True
