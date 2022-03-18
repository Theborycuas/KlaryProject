from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(Tag, TagAdmin)