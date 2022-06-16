from django.contrib import admin

from .models import GoodItems, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(GoodItems)
class GoodItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'created_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('title',)}
