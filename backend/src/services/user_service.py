from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User
from src.rest.managers.user_manager import UserManager
from src.services.auth_service import AuthService
from src.services.email_service import EmailService


class UserService:
    @staticmethod
    def generate_confirmation_url(user_id: int) -> str:
        token = AuthService.create_token(user_id=user_id, token_type='access')
        return f'/api/v1/confirm/{token}'

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
        # todo prepare a beautiful message
        confirmation_url = cls.generate_confirmation_url(user_id=user.id)
        EmailService.send_email(receiver=user.email, message=confirmation_url)
