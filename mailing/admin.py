from django.contrib import admin

from .models import Message, Mailing, Log


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'is_published')
    list_filter = ('title', 'is_published')
    search_fields = ('title',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('send_name', 'message', 'start_time', 'end_time', 'frequency', 'status')
    list_filter = ('send_name', 'status')
    search_fields = ('send_name',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'send_time', 'attempt_status')
