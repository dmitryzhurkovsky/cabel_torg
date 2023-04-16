import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.core import settings


class EmailService:
    @classmethod
    def send_email(cls, receiver: str, message: str, subject: str, html_message: str = None):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = settings.SMTP_EMAIL_SENDER
            msg['To'] = receiver
            msg.attach(MIMEText(message, 'plain'))
            if html_message:
                msg.attach(MIMEText(html_message, 'html'))

            client = smtplib.SMTP(settings.SMTP_HOST)
            client.sendmail(from_addr=settings.SMTP_EMAIL_SENDER, to_addrs=(receiver,), msg=msg.as_string())
            client.quit()
        except smtplib.SMTPException:
            print("Error: unable to send email")
            # todo add logging
