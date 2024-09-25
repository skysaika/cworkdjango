from django.contrib import admin

from vlog.models import VlogPost


@admin.register(VlogPost)
class VlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'is_published', 'view_count', 'owner')
    list_filter = ('created', 'is_published', 'owner')
