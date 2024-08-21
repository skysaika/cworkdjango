from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'is_published')
    list_filter = ('title', 'is_published')
    search_fields = ('title',)
