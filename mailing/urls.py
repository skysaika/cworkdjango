from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from mailing.apps import MailingConfig
from mailing.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView, LogListView, \
    LogDetailView

app_name = MailingConfig.name


urlpatterns = [
    path('message_list/', cache_page(60)(MessageListView.as_view()), name='message_list'),  # список сообщений
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),  # просмотр сообщения
    path('message_create/', MessageCreateView.as_view(), name='message_create'),  # создание сообщения
    path('message_edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),  # редактирование сообщения
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),  # удаление сообщения
    # path('message_publish/<int:pk>/toggle_publish/', toggle_publish, name='toggle_publish'),  # публикация сообщения

    path('mailing_list/', cache_page(60)(MailingListView.as_view()), name='mailing_list'),  # список рассылок
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),  # просмотр рассылки
    path('mailing_create/', never_cache(MailingCreateView.as_view()), name='mailing_create'),  # создание рассылки
    path('mailing_edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),  # редактирование рассылки
    path('mailing_delete/<int:pk>/', never_cache(MailingDeleteView.as_view()), name='mailing_delete'),  # удаление рассылки

    path('log_list/', LogListView.as_view(), name='log_list'),  # список логов
    path('log_detail/<int:pk>/', LogDetailView.as_view(), name='log_detail'),  # просмотр лога

]
