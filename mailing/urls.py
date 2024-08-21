from django.urls import path


from mailing.apps import MailingConfig
from mailing.views import MessageListView

app_name = MailingConfig.name


urlpatterns = [
    path('message_list/', MessageListView.as_view(), name='message_list'),  # список сообщений
]
