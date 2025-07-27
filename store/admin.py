from django.contrib import admin
from .models import Category, Sticker
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Sticker)
class StickerAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    list_filter = ("category",)