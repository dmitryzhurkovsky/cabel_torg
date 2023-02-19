from src.managers.base_manager import CRUDManager
from src.models.service_entities.article_model import Article
from src.models.service_entities.delivery_type_model import DeliveryType
from src.models.service_entities.partner_model import Partner
from src.models.service_entities.vender_info_model import Address, VendorInfo


class ArticleManager(CRUDManager):
    table = Article


class DeliveryTypeManager(CRUDManager):
    table = DeliveryType


class PartnerManager(CRUDManager):
    table = Partner


class AddressManager(CRUDManager):
    table = Address


class VendorInfoManager(CRUDManager):
    table = VendorInfo
