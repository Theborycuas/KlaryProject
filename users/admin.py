from django.contrib import admin
from .models import UserApp

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(UserApp, UserAdmin)