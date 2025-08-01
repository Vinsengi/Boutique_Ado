from django.contrib import admin
from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    list_filter = ('category',)
    search_fields = ('sku', 'name', 'description', 'category__name'
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
