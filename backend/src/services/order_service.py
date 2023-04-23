from dateutil.relativedelta import relativedelta

from src.core import settings
from src.invoice_generator.main import InvoiceGenerator
from src.models import User, Order
from src.models.order_model import OrderStatus
from src.services.email_service import EmailService


class OrderService:
    ORDER_VERBOSE_NAMES = {
        OrderStatus.IN_PROCESSING: 'В процессе',
        OrderStatus.SENT: 'Отправлен',
        OrderStatus.CANCELED: 'Отменен',
        OrderStatus.COMPLETED: 'Завершен',
    }

    @classmethod
    async def send_create_order(cls, user: User, order: Order):
        template = settings.templates.get_template('email/create_order.htm')
        message = f"""
            Добрый день {user.full_name}. Заказ с номером {order.number} был успешно создан. 
            Заказанные товары уже готовятся к отправке, с вами свяжется специалист для уточнения.
            Отслеживать статус заказа в реальном времени можно в Личном кабинете.
            Желаем Вам приятных покупок!
        """
        invoice: bytes = await InvoiceGenerator.generate_invoice(order_id=order.id)
        html_message = template.render({
            'name': user.full_name,
            'order_number': order.number,
            'phone_number': user.phone_number,
            'pick_up_point': order.delivery_type.payload,
            'delivery date': order.created_at + relativedelta(days=3),

            'static_url': settings.STATIC_PATH
        })

        EmailService.send_email(
            receiver=user.email,
            message=message,
            html_message=html_message,
            subject='Ваш заказ создан!',
            attachments=[('invoice.pdf', invoice)],
            send_to_admin=True
        )

    @classmethod
    async def send_change_order_status(cls, user: User, order: Order):
        template = settings.templates.get_template('email/change_order_status.htm')
        order_status_verbose_name = cls.ORDER_VERBOSE_NAMES[order.status]
        message = f"""
            Добрый день {user.full_name}. Уведомляем Вас, что статус вашего заказа изменен!. 
            Номер заказа {order.number}. Статус заказа {order_status_verbose_name}.
        """
        html_message = template.render({
            'name': user.full_name,
            'order_number': order.number,
            'order_status': order_status_verbose_name,
            'static_url': settings.STATIC_PATH
        })

        EmailService.send_email(
            receiver=user.email,
            message=message,
            html_message=html_message,
            subject=f'Статус заказа {order.number} изменен',
        )
