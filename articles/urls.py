from django.urls import path
from articles.views import (
        home, 
        detail, 
        search_view, 
        create_article_view,
        edit_article_view
    )


app_name = "articles"

urlpatterns = [
    path("", home, name="home"),
    path("article/<int:id>", detail, name="article-detail"),
    path("search", search_view, name="article-search"),
    path("create/article", create_article_view, name="article-create"),
    path("edit/article/<int:id>", edit_article_view, name="article-edit")
]