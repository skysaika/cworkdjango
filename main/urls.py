from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import IndexView

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='index'),  # Главная закеширована на 60 с
]
