from django.views.generic import ListView
from .models import Message


class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message_list.html'


