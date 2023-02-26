from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ENUM as pgEnum

from src.core.enums import BaseEnum
from src.models.abstract_model import BaseModel


class RequestCallType(str, BaseEnum):
    UNSET = 'U'
    GOOD_RECEIPT = 'GR'


class RequestCall(BaseModel):
    __tablename__ = 'service__request_call'

    fullname = Column(String)
    phone_number = Column(String(50))
    type = Column('type', pgEnum(*RequestCallType.values(), name='request_call_status'), default=RequestCallType.UNSET)
