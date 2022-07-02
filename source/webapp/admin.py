from django.contrib import admin

from .models import Record


class RecordsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_at']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['author', 'mail', 'description', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Record, RecordsAdmin)
