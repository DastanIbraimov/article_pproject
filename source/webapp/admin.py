from django.contrib import admin

from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'published_at']
    list_filter = ['published_at', 'author']
    date_hierarchy = 'published_at'
    search_fields = ['title', 'content']
    readonly_fields = ['published_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
