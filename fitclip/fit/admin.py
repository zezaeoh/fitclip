from django.contrib import admin

# Register your models here.
from .models.fit_spec import FitSpec, FitSpecOption


@admin.register(FitSpec)
class FitSpecAdmin(admin.ModelAdmin):
    pass


class FitSpecOptionInline(admin.StackedInline):
    model = FitSpecOption
    extra = 1
