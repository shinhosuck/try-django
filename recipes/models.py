from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from recipes.utils import (
    validate_ingredient_unit, 
    string_to_float,
    number_str_to_float
)
from django.db import models



class Recipe(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    directions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta: 
        ordering = ["-id"]

    def __str__(self):
        return self.title
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    quanity = models.CharField(max_length=120)
    unit = models.CharField(max_length=120, validators=[validate_ingredient_unit])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # description = models.TextField()
    


    def save(self, *args, **kwargs):
        input_data, to_float_success = number_str_to_float(self.quanity)
        if to_float_success:
            self.quanity = input_data
        else:
            self.quanity = ""
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.recipe}"