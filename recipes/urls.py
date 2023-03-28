from django.urls import path 
from recipes.views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_update_view
)

app_name = "recipes"


urlpatterns = [
    path("list", recipe_list_view, name="list"),
    path("detail/<int:id>", recipe_detail_view, name="detail"),
    path("update/<int:id>", recipe_update_view, name="update")
]