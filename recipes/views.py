from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe, RecipeIngredient
from recipes.forms import RecipeForm, IngredientForm
from django.forms.models import modelformset_factory
import pint 



def recipe_list_view(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes/list.html", context)


def recipe_detail_view(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.recipeingredient_set.all()
    context = {"recipe": recipe}
    return render(request, "recipes/detail.html", context)


def recipe_create_view(request):
    # IngredientFormSet = modelformset_factory(RecipeIngredient, form=IngredientForm, extra=0)
    # ingredient_forms = IngredientFormSet(request.POST or None, queryset=None)
    # ingredient_form = IngredientForm(request.POST or None)
    recipe_form = RecipeForm(request.POST or None)
    ingredient_form = IngredientForm(request.POST or None)

    context = {
            "recipe_form": recipe_form,
             "ingredient_form": ingredient_form,
        }

    if recipe_form.is_valid() and ingredient_form.is_valid():
            
        new_recipe = recipe_form.save(commit=False)
        new_ingredient = ingredient_form.save(commit=False)

        new_recipe.user = request.user
        new_ingredient.recipe = new_recipe

        new_recipe.save()
        new_ingredient.save()
        
        recipe = get_object_or_404(Recipe, id=new_recipe.id)
        ingredients = recipe.recipeingredient_set.all()

        IngredientFormSet = modelformset_factory(RecipeIngredient, form=IngredientForm, extra=10)
        ingredient_forms = IngredientFormSet(request.POST or None, queryset=ingredients)
        context["ingredient_forms"] = ingredient_forms

        if ingredient_forms.is_valid(): 
            new_ingredient = ingredient_forms.save(commit=False)
            new_ingredient.recipe = new_recipe
        # return redirect("recipes:detail", new_recipe.id)
    print(ingredient_forms)
    return render(request, "recipes/create.html", context)


def recipe_update_view(request, id=None):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.recipeingredient_set.all()
    IngredientFormSet = modelformset_factory(RecipeIngredient, 
                        form=IngredientForm, extra=0)
    ingredient_forms = IngredientFormSet(request.POST or None, queryset=ingredients)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    context = {
            "recipe_form": recipe_form,
            "ingredient_forms": ingredient_forms,
            "recipe": None
        }
    if recipe_form.is_valid() and ingredient_forms.is_valid():
        recipe_form.save()
        for form in ingredient_forms:
            form.save()
        context["recipe"] = recipe
        # return redirect("recipes:update", id=id)
    return render(request, "recipes/update.html", context)



