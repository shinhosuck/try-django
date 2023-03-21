from django import forms
from articles.models import Article


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]