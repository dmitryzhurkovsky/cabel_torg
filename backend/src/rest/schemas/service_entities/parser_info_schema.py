from datetime import datetime

from pydantic import BaseModel


class ParserInfoSchema(BaseModel):
    started_at: datetime | None
    finished_at: datetime | None
    files_were_updated_at: datetime | None
    is_failed: bool
    exception: str | None

    class Config:
        orm_mode = True
