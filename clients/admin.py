from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Админка модели клиента"""
    list_display = ('email', 'first_name', 'last_name', 'comment', 'is_active', 'owner')
    list_filter = ('email', 'is_active', 'owner')
    search_fields = ('email',)
