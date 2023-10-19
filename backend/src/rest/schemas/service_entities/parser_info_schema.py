from datetime import datetime

from pydantic import BaseModel


class ParserInfoSchema(BaseModel):
    started_at: datetime | None = None
    finished_at: datetime | None = None
    files_were_updated_at: datetime | None = None
    is_failed: bool
    exception: str | None = None

    class Config:
        from_attributes = True
