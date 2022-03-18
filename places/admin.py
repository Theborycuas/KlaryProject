from django.contrib import admin
from .models import Place

class CityAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(Place, CityAdmin)