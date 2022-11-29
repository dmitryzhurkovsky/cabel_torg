from pydantic import BaseModel


class ProductInWatchListSchema(BaseModel):
    user_id: int | None = None  # We don't validate user_id because we rewrite it by user_id from request
    product_id: int

    class Config:
        orm_mode = True
