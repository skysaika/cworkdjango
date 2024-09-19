from celery import shared_task
from django.core.mail import send_mail
from .models import Mailing, Log

@shared_task
def send_mailing(mailing_id):
    mailing = Mailing.objects.get(id=mailing_id)

    # Получаем связанных клиентов
    clients = mailing.message.recipient.all()  # Изменила на `recipient` из `Message`
    subject = mailing.message.title  # Заголовок сообщения
    message = mailing.message.body  # Текст сообщения

    try:
        # Отправляем письмо
        server_response = send_mail(
            subject=subject,
            message=message,
            from_email='skysaika@yandex.ru',
            recipient_list=[client.email for client in clients]
        )
        # Записываем лог в случае успеха
        Log.objects.create(
            mailing=mailing,
            attempt_status='success',
            server_response=str(server_response)
        )
    except Exception as e:
        # Записываем лог в случае неудачи
        Log.objects.create(
            mailing=mailing,
            attempt_status='failed',
            server_response=str(e)
        )
