from sqlalchemy import Column, String

from src.models.abstract_model import BaseModel


class Article(BaseModel):
    __tablename__ = 'service__articles'

    title = Column(String(255))
    content = Column(String, nullable=True)
    image = Column(String, nullable=True)
    preview_text = Column(String, nullable=True)
