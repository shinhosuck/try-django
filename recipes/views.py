from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe, RecipeIngredient
from recipes.forms import RecipeForm
import pint 



def recipe_list_view(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes/list.html", context)


def recipe_detail_view(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {"recipe": recipe}
    return render(request, "recipes/detail.html", context)


def recipe_update_view(request, id=None):
    recipe = get_object_or_404(Recipe, id=id)
    form = RecipeForm(request.POST or None, instance=recipe)
    context = {
            "form": form,
            "recipe": None
        }
    if form.is_valid():
        form.save()
        context["recipe"] = recipe
    return render(request, "recipes/create_or_update.html", context)



