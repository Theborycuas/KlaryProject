from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(City, CityAdmin)