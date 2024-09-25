from django.conf import settings
from django import template
from django.core.mail import send_mail
from clients.models import Client
from mailing.models import Mailing, Message, Log
register = template.Library()


def send_email(*args):
    all_email = []
    for client in Client.objects.all():
        all_email.append(str(client.email))

    for mailing in Mailing.objects.all():
        log = Log(mailing=mailing, attempt_status=Log.SUCCESS)
        log.save()

        if mailing.status == Mailing.CREATED and mailing.frequency == (str(*args)):
            filtered_messages = mailing.message
            message = Message.objects.filter(subject=filtered_messages)

            for msg in message:
                send_mail(
                    subject=msg.subject,
                    message=msg.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*all_email],
                )
                status_list = []
                server_response = {
                    'mailing': Mailing.objects.get(pk=mailing.id),
                    'attempt_status': Log.SUCCESS,
                    'server_response': [*all_email]
                }
                status_list.append(Log(**server_response))
                Log.objects.bulk_create(status_list)
                if mailing.frequency == Mailing.ONCE:
                    mailing.status = Mailing.COMPLETED
                    mailing.save()
                else:
                    mailing.status = Mailing.RUNNING
                    mailing.save()
