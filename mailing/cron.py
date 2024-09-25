# import datetime

from django.conf import settings
from django.core.mail import send_mail

from clients.models import Client
from mailing.models import Mailing, Message, Log


def my_func_daily():
    print('daily')


def my_func_weekly():
    print('weekly')


def my_func_monthly():
    print('monthly')

def my_func_once():
    print('once')

# def launch_new_mailing():
#     curr_date = datetime.now()
#
#     mailing_new = Mailing.objects.filter(
#         status=Mailing.CREATED,
#         start_time__lte=curr_date,
#         end_time__gte=curr_date
#     )
#
#     if mailing_new.exists():
#         for new_mailing in mailing_new:
#             new_mailing.status = Mailing.RUNNING
#             new_mailing.save()
#
#
# def stop_finished_mailings():
#     curr_date = datetime.now()
#
#     mailings_finished = Mailing.objects.filter(
#         status=Mailing.RUNNING,
#         end_time__lte=curr_date
#     )
#
#     if mailings_finished.exists():
#         for new_mailing in mailings_finished:
#             new_mailing.status = Mailing.COMPLETED
#             new_mailing.save()
#
#
# def prepare_mailings():
#     launch_new_mailing()
#     stop_finished_mailings()
#
#
# def send_mail_job():
#     err_count = len([err for err, _ in reports if err])
#     total_count = len(reports)
#     if err_count == total_count:
#         print(f'Все рассылки завершены. Ошибок: {err_count}')
#     else:
#         print(f'Все рассылки завершены. Ошибок: {err_count} из {total_count}')


# def send_email(*args):
#     all_email = []
#     for client in Client.objects.all():
#         all_email.append(str(client.email))
#
#     for mailing in Mailing.objects.all():
#         if mailing.status == Mailing.CREATED and mailing.frequency == (str(*args)):
#             filtered_messages = mailing.message
#             message = Message.objects.filter(subject=filtered_messages)
#
#             for msg in message:
#                 send_mail(
#                     subject=msg.subject,
#                     message=msg.body,
#                     from_email=settings.EMAIL_HOST_USER,
#                     recipient_list=[*all_email],
#                 )
#                 status_list = []
#                 server_response = {
#                     'mailing': Mailing.objects.get(pk=mailing.id),
#                     'attempt_status': Log.SUCCESS,
#                     'server_response': [*all_email]
#                 }
#                 status_list.append(Log(**server_response))
#                 Log.objects.bulk_create(status_list)
#                 if mailing.frequency == Mailing.ONCE:
#                     mailing.status = Mailing.COMPLETED
#                     mailing.save()
#                 else:
#                     mailing.status = Mailing.RUNNING
#                     mailing.save()
