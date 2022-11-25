from django.contrib import admin
from articles.models import Article


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#     search_fields = ['title']

# admin.site.register(Article, #ArticleAdmin)

admin.site.register(Article)
