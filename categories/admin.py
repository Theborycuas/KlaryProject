from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(Category, CategoryAdmin)