from recipes.models import Recipe, RecipeIngredient
from django import forms 


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "directions"]