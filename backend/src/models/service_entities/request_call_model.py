from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM as pgEnum

from src.core.enums import BaseEnum
from src.models.abstract_model import BaseModel


class RequestCallType(str, BaseEnum):
    UNSET = 'U'
    GOODS_RECEIPT = 'GR'

    @classmethod
    def description(cls) -> str:
        return 'U - Unset. It\' used for all request calls.' \
               'GD - Good Receipt. It\'s used for notify about the receipt of goods in the warehouse.'


class RequestCall(BaseModel):
    __tablename__ = 'service__request_call'

    fullname = Column(String)
    phone_number = Column(String(50))
    type = Column('type', pgEnum(*RequestCallType.values(), name='request_call_status'), default=RequestCallType.UNSET)

    product_id = Column(Integer, ForeignKey('products.id'))

