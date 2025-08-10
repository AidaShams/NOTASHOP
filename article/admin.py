from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    readonly_fields = ('created_at',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'is_published')
    list_filter = ('is_published', 'publish_date')
    search_fields = ('title', 'description', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'writer', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('writer__username', 'comment')
    readonly_fields = ('created_at',)