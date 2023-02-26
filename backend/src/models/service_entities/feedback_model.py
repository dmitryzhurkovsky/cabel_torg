from sqlalchemy import Column, String

from src.models.abstract_model import BaseModel


class Feedback(BaseModel):
    __tablename__ = 'service__feedback'

    fullname = Column(String)
    email = Column(String(255))
    phone_number = Column(String(50))
    message = Column(String)
