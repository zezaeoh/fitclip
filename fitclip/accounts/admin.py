from django.contrib import admin

# Register your models here.
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_location', 'date_joined', 'updated_on')


admin.site.register(UserProfile, UserProfileAdmin)
