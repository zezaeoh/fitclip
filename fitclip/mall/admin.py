from django.contrib import admin

# Register your models here.
from .models.product import Product, ProductDetail
from .models.shop import Shop
from .models.category import Category, Section, Sub
from ..fit.admin import FitSpecOptionInline


class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    exclude = ('_meta_data',)


class SectionInline(admin.StackedInline):
    model = Section
    extra = 1


class SubInline(admin.StackedInline):
    model = Sub
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDetailInline]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [SubInline]


@admin.register(Sub)
class SubAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'category')
    inlines = [FitSpecOptionInline]

