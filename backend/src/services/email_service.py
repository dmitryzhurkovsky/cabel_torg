import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.core import settings


class EmailService:
    @classmethod
    def send_email(
            cls,
            receiver: str,
            message: str,
            subject: str,
            send_to_admin: bool = False,
            html_message: str = None,
            attachments: list[tuple[str, bytes]] = None  # list[file_name, content]
    ):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = settings.SMTP_EMAIL_SENDER
            msg['To'] = receiver
            msg.attach(MIMEText(message, 'plain'))

            send_to = [receiver]
            if send_to_admin:
                send_to += settings.ADMINISTRATOR_EMAIL

            if html_message:
                msg.attach(MIMEText(html_message, 'html'))
            if attachments:
                for attachment in attachments:
                    extension = attachment[0].split('.')[-1]
                    attached_file = MIMEApplication(attachment[1], _subtype=extension)
                    attached_file.add_header('content-disposition', 'attachment', filename=attachment[0])
                    msg.attach(attached_file)

            client = smtplib.SMTP(settings.SMTP_HOST)
            client.sendmail(from_addr=settings.SMTP_EMAIL_SENDER, to_addrs=send_to, msg=msg.as_string())
            client.quit()
        except smtplib.SMTPException:
            print("Error: unable to send email")
            # todo add logging
