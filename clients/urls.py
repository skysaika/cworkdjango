from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientListView, ClientDetailView

app_name = ClientsConfig.name

urlpatterns = [
    path('client_list/', ClientListView.as_view(), name='client_list'),  # список клиентов
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),  # просмотр клиента
]
