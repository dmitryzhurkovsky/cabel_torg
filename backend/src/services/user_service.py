from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.models import User
from src.rest.managers.user_manager import UserManager
from src.services.auth_service import AuthService
from src.services.email_service import EmailService

template = settings.templates.get_template('registration.html')


class UserService:
    @staticmethod
    def generate_confirmation_url(user_id: int) -> str:
        token = AuthService.create_token(user_id=user_id, token_type='access')
        return f'{settings.SITE_HOST}/api/v1/confirm/{token}'

    @classmethod
    async def confirm_user(cls, token: str, session: AsyncSession):
        user_id = AuthService.decode_token(token=token)
        await UserManager.update(
            session=session,
            pk=user_id,
            input_data={
                'is_active': True
            }
        )

    @classmethod
    def send_confirmation_url(cls, user: User):
        confirmation_url = cls.generate_confirmation_url(user_id=user.id)
        message = f"""
            Добрый день {user.full_name}. Регистрация прошла успешно. 
            Чтобы активировать аккаунт перейдите по ссылке {confirmation_url}.
            Желаем Вам приятных покупок!
        """
        html_message = template.render({
            'name': user.full_name,
            'confirmation_url': confirmation_url,
            'static_url': f'{settings.STATIC_PATH}/registration'
        })
        EmailService.send_email(
            receiver=user.email,
            message=message,
            html_message=html_message,
            subject='Закончите регистрацию'
        )
