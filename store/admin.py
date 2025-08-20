from django.contrib import admin
from django.utils.html import format_html
from .models import Sticker, Category


# Register your models here.

@admin.register(Sticker)
class StickerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'price', 'stock', 'is_active']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'tags', 'description']

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:50px; height:auto;" />', obj.image.url)
        return "No Image"
    thumbnail_preview.short_description = "Image"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    search_fields = ['name']

# did this to customise and give it more features and make it more user-friendly
