from django.contrib import admin

# Register your models here.
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_location', 'date_joined', 'updated_on')

