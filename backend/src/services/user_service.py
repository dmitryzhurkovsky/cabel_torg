from src.core import settings
from src.models import User
from src.services.auth_service import AuthService
from src.services.email_service import EmailService


class UserService:
    @staticmethod
    def generate_confirmation_url(user_id: int) -> str:
        token = AuthService.create_token(user_id=user_id, token_type='access')
        return f'{settings.SITE_HOST}/api/v1/confirm/{token}'

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

    @classmethod
    def send_new_password(cls, user: User, new_password: str):
        context = {
            'static_url': settings.STATIC_PATH,
            'name': user.full_name,
            'email': user.email,
            'generated_password': new_password
        }
        message = f"""
            Добрый день {user.full_name}. . 
            Ваш пароль был изменен на успешно изменен!
            Новый парль {new_password}
        """

        template_path = 'email/reset_password.html'
        template = settings.templates.get_template(template_path)
        html_message = template.render(context)

        EmailService.send_email(
            receiver=user.email,
            message=message,
            html_message=html_message,
            subject='Изменение пароля'
        )
