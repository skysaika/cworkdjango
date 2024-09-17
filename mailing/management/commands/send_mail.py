import datetime
import logging
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from mailing.models import Mailing, Log

# Настройка логирования
logging.basicConfig(filename='mailing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(BaseCommand):
    help = 'Send scheduled mailings'

    def handle(self, *args, **options):
        now = datetime.datetime.now().date()
        mailings = Mailing.objects.filter(start_time__lte=now, end_time__gte=now, status='RUNNING')

        for mailing in mailings:
            try:
                recipient_list = [client.email for client in mailing.message.recipient.all() if client.email]
                if recipient_list:
                    send_mail(
                        subject=mailing.send_name,
                        message=mailing.message.body,
                        from_email='skysaika@yandex.ru',
                        recipient_list=recipient_list,
                        fail_silently=False
                    )
                    # Запись в лог об успешной попытке
                    Log.objects.create(
                        mailing=mailing,
                        attempt_status=Log.SUCCESS,
                        server_response='Email successfully sent.'
                    )
                    logging.info(f"Mailing '{mailing.send_name}' sent successfully.")
                else:
                    logging.warning(f"No recipients for mailing '{mailing.send_name}'.")
            except Exception as e:
                # Запись в лог о неудачной попытке
                Log.objects.create(
                    mailing=mailing,
                    attempt_status=Log.FAILED,
                    server_response=str(e)
                )
                logging.error(f"Error sending mailing '{mailing.send_name}': {str(e)}")
