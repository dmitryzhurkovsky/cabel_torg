import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.core import settings
from src.log import create_logger

smtp_logger = create_logger('smtp')


class EmailService:
    @classmethod
    def send_email(
            cls,
            message: str,
            subject: str,
            receiver: str = None,
            send_to_admin: bool = False,
            send_to_service: bool = False,
            html_message: str = None,
            attachments: list[tuple[str, bytes]] = None  # list[file_name, content]
    ):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = settings.SMTP_EMAIL_SENDER
            if receiver:
                msg['To'] = receiver
            elif not receiver and send_to_service:
                msg['To'] = settings.SERVICE_EMAIL
            elif not receiver and send_to_admin:
                msg['To'] = settings.ADMINISTRATOR_EMAIL

            msg.attach(MIMEText(message, 'plain'))

            send_to = []
            if receiver:
                send_to += receiver
            else:
                if send_to_service:
                    send_to += settings.SERVICE_EMAIL
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
            smtp_logger.info(
                f"Error: unable to send email for {receiver},\n"
                f"Subject is {subject},\n"
                f"message is {message}\n\n"
            )
        except OSError:
            smtp_logger.info(
                "Backend can't connect to SMTO server"
            )
