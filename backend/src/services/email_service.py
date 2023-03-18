import smtplib

from src.core import settings


class EmailService:
    @property
    def client(self) -> smtplib.SMTP:
        return smtplib.SMTP()

    @classmethod
    def send_email(cls, receiver: str, message: str):
        try:
            cls.client.connect()
            cls.client.sendmail(settings.SMTP_SENDER_EMAIL, receiver, message)
        except smtplib.SMTPException:
            print("Error: unable to send email")
            # todo add logging
