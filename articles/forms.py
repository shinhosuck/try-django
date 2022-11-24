from django import forms
from articles.models import Article

class OldArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data # this is a dictionary
        print(cleaned_data)
        return cleaned_data


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content']