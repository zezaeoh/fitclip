from django.contrib import admin

# Register your models here.
from .models.fit_spec import FitSpec, FitSpecOption
from .models.personal_fit import PersonalFitUIOption, PersonalFit


@admin.register(FitSpec)
class FitSpecAdmin(admin.ModelAdmin):
    pass


class FitSpecOptionInline(admin.StackedInline):
    model = FitSpecOption
    extra = 1


@admin.register(PersonalFit)
class PersonalFitAdmin(admin.ModelAdmin):
    pass


class PersonalFitUIOptionInline(admin.StackedInline):
    model = PersonalFitUIOption
    extra = 1
