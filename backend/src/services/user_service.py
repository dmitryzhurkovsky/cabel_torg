from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.models import User
from src.rest.managers.user_manager import UserManager
from src.services.auth_service import AuthService
from src.services.email_service import EmailService


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
    def send_confirmation_url(cls, user: User, generated_password: str = None):
        context = {
            'static_url': settings.STATIC_PATH,
            'name': user.full_name
        }
        message = f"""
            Добрый день {user.full_name}. Регистрация прошла успешно. 
            Желаем Вам приятных покупок!
        """
        if generated_password:
            template_path = 'email/registration_with_generated_password.html'
            context |= {
                'generated_password': generated_password,
                'email': user.email
            }
            message += f'Логин {user.email}, пароль {generated_password}'
        else:
            template_path = 'email/registration.html'

        template = settings.templates.get_template(template_path)
        html_message = template.render(context)
        EmailService.send_email(
            receiver=user.email,
            message=message,
            html_message=html_message,
            subject='Регистрация прошла успешно'
        )
