from sqlalchemy import Column, String

from src.core import settings
from src.models.abstract_model import BaseModel


class Article(BaseModel):
    __tablename__ = 'articles'

    title = Column(String(255))
    content = Column(String, nullable=True)
    image = Column(String, nullable=True)

    @property
    def preview_text(self) -> str:
        return self.content[:settings.PREVIEW_CONTENT_LENGTH] if self.content else ''
