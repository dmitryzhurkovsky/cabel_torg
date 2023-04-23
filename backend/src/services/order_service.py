from dateutil.relativedelta import relativedelta

from src.core import settings
from src.models import User, Order
from src.services.email_service import EmailService

template = settings.templates.get_template('create_order.htm')


class OrderService:
    @classmethod
    def send_order_confirmation(cls, user: User, order: Order):
        message = f"""
            Добрый день {user.full_name}. Заказ с номером {order.number} был успешно создан. 
            Заказанные товары уже готовятся к отправке, с вами свяжется специалист для уточнения.
            Отслеживать статус заказа в реальном времени можно в Личном кабинете.
            Желаем Вам приятных покупок!
        """
        html_message = template.render({
            'name': user.full_name,
            'order_number': order.number,
            'phone_number': user.phone_number,
            'pick_up_point': order.delivery_type.payload,
            'delivery date': order.created_at + relativedelta(days=3),

            'static_url': settings.STATIC_PATH
        })
        EmailService.send_email(
            receiver=user.email, message=message, html_message=html_message, subject='Ващ заказ создан!'
        )
