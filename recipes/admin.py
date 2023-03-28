from django.contrib import admin
from recipes.models import Recipe, RecipeIngredient



class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    # fields = ["name"]
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    search_fields = ["title"]
    raw_id_fields = ["user"]
    readonly_fields = ["created", "updated"]
    list_display = ["id", "title", "slug", "created", "updated"]

admin.site.register(Recipe, RecipeAdmin)


# class RecipeIngredientAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]
#     readonly_fields = ["created", "updated"]
#     search_fields = ["title"]
    

# admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

