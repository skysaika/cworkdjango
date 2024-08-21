from django.urls import path


from mailing.apps import MailingConfig
from mailing.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView

app_name = MailingConfig.name


urlpatterns = [
    path('message_list/', MessageListView.as_view(), name='message_list'),  # список сообщений
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),  # просмотр сообщения
    path('message_create/', MessageCreateView.as_view(), name='message_create'),  # создание сообщения
    path('message_edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),  # редактирование сообщения
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),  # удаление сообщения

    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),  # список рассылок
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),  # просмотр рассылки
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),  # создание рассылки
    path('mailing_edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),  # редактирование рассылки
]
