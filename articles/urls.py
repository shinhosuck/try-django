from django.urls import path
from articles.views import(
    home,
    about,
    search,
    article_detail,
    create_article,
    user_login,
    user_logout,
    user_register
)


app_name = 'articles'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('search', search, name='search'),
    path('article/detail/<int:pk>', article_detail, name='article-detail'),
    path('create/article', create_article, name='create-article'),
    path('register', user_register, name='register'),
    path('login', user_login, name='user-login'),
    path('logout', user_logout, name='user-logout')
]