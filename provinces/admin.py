from django.contrib import admin
from .models import Province

class ProvinceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(Province, ProvinceAdmin)