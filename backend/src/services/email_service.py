import smtplib

from src.core import settings


class EmailService:
    @classmethod
    def send_email(cls, receiver: str, message: str):
        try:
            client = smtplib.SMTP('localhost')
            client.sendmail(settings.SMTP_SENDER_EMAIL, receiver, message)
        except smtplib.SMTPException:
            print("Error: unable to send email")
            # todo add logging
