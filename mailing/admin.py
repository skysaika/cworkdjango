from django.contrib import admin

from .models import Message, Mailing, Log


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'is_published', 'owner')
    list_filter = ('title', 'is_published', 'owner')
    search_fields = ('title',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id','send_name', 'message', 'start_time', 'end_time', 'frequency', 'status', 'owner')
    list_filter = ('send_name', 'status', 'owner')
    search_fields = ('send_name',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'mailing_id', 'send_time', 'attempt_status')

