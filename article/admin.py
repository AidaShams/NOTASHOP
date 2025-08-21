from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    readonly_fields = ('created_at',)
    fields = ('writer', 'comment', 'is_approved', 'created_at')
    can_delete = True
    show_change_link = True


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'publish_date', 'is_published')
    readonly_fields = ('slug',)
    list_filter = ('is_published', 'publish_date', 'author')
    search_fields = ('title', 'description', 'author__username')
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'writer', 'created_at', 'is_approved')
    readonly_fields = ('created_at',)
    list_filter = ('is_approved', 'created_at')
    search_fields = ('writer__username', 'comment')
    actions = ['approve_comments']

    #approve multiple comments at once
    def approve_comments(self, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Mark selected comments as approved"