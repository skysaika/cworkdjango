from django.shortcuts import render
from django.views.generic import ListView

from clients.models import Client


# Create your views here.
class ClientListView(ListView):
    """Просмотр списка клиентов"""
    model = Client
    template_name = 'clients/client_list.html'
    extra_context = {
        'title': 'Список клиентов'
    }
