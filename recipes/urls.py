from django.urls import path 
from recipes.views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_update_view,
    recipe_create_view
)

app_name = "recipes"


urlpatterns = [
    path("list", recipe_list_view, name="list"),
    path("<int:id>/detail", recipe_detail_view, name="detail"),
    path("<int:id>/update", recipe_update_view, name="update"),
    path("create", recipe_create_view, name="create")
]