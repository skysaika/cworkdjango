from django.urls import path
from django.views.decorators.cache import cache_page

from vlog.apps import VlogConfig
from vlog.views import VlogPostCreateView, VlogPostListView, VlogPostDetailView, VlogPostUpdateView, VlogPostDeleteView

app_name = VlogConfig.name


urlpatterns = [
    path('create_post/', VlogPostCreateView.as_view(), name='create_post'),  # создание поста
    path('post_list/', cache_page(60)(VlogPostListView.as_view()), name='post_list'),  # список постов закеширован
    path('edit_post/<int:pk>/', VlogPostUpdateView.as_view(), name='edit_post'),  # редактирование поста
    path('post_detail/<int:pk>/', VlogPostDetailView.as_view(), name='post_detail'),  # карточка поста
    path('delete_post/<int:pk>/', VlogPostDeleteView.as_view(), name='delete_post'),  # удаление поста
]
