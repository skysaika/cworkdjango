from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientListView

app_name = ClientsConfig.name

urlpatterns = [
    path('client_list/', ClientListView.as_view(), name='client_list'),  # список клиентов
]
