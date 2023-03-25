from sqlalchemy import Column, String, Boolean

from src.models.abstract_model import BaseModel


class Banner(BaseModel):
    __tablename__ = 'service__banners'

    title = Column(String(255))
    subtitle = Column(String, nullable=True)
    text = Column(String, nullable=True)
    preview_text = Column(String, nullable=True)
    image = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
