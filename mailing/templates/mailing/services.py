from django.conf import settings

from clients.models import Client
from mailing.models import Mailing, Message, Log


def send_mail(*args, **kwargs):
    all_email = []

    for client in Client.objects.all():
        all_email.append(str(client.email))

    for mailing in Mailing.objects.all():
        if mailing.status == Mailing.CREATED and mailing.frequency == (str(*args)):
            filtered_message = str(mailing.message)
            message = Message.objects.filter(subject=filtered_message)
            for msg in message:
                send_mail(
                    title=msg.title,
                    body=msg.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*all_email],
                )
                status_list = []
                server_response = {
                    'mailing': Mailing.objects.get(pk=mailing.pk),
                    'attempt_status': Log.SUCCESS,
                    'server_response': [*all_email]}
                status_list.append(Log(**server_response))
                Log.objects.bulk_create(status_list)
                if mailing.frequency ==Mailing.ONCE:
                    mailing.status = Mailing.COMPLETED
                    mailing.save()
                else:
                    mailing.status = Mailing.RUNNING
                    mailing.save()

