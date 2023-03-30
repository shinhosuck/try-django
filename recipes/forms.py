from recipes.models import Recipe, RecipeIngredient
from django import forms 


class RecipeForm(forms.ModelForm):
    required_css_class = "required-field"
    error_css_class = "error-field"
    # title = forms.CharField(widget=forms.TextInput(attrs={"class": "title-field", "id": "new-title"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"class": "description-field"}))
    # directions = forms.CharField(widget=forms.Textarea(attrs={"class": "directions-field"}))

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "title-field", "id": "new-title"}), help_text="Need help! <a href='/'>Contact us</a>")

    class Meta:
        model = Recipe
        fields = ["title", "description", "directions"]

    # or use init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "new-title-field", "placeholder": "New title"})
        self.fields["description"].widget.attrs.update({"class": "new-description-field", "rows": "5"})
        # super().save(*args, **kwargs)


class IngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["name", "quanity", "unit"]