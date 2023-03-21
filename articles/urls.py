from django.urls import path, include
from articles.views import (
        home, 
        detail, 
        search_view, 
        new_article_view
    )


app_name = "articles"

urlpatterns = [
    path("", home, name="home"),
    path("article/<int:id>", detail, name="article-detail"),
    path("search", search_view, name="article-search"),
    path("new/article", new_article_view, name="article-new"),
]