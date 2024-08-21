from django.urls import path


from mailing.apps import MailingConfig
from mailing.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView

app_name = MailingConfig.name


urlpatterns = [
    path('message_list/', MessageListView.as_view(), name='message_list'),  # список сообщений
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),  # просмотр сообщения
    path('message_create/', MessageCreateView.as_view(), name='message_create'),  # создание сообщения
    path('message_edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),  # редактирование сообщения
]
