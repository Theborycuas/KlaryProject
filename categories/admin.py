from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Category, CategoryAdmin)