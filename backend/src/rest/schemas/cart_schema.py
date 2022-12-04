from pydantic import BaseModel


class ProductInCartSchema(BaseModel):
    user_id: int | None = None  # We don't validate user_id because we rewrite it by user_id from request
    product_id: int
    amount: int

    class Config:
        orm_mode = True
