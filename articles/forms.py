from django import forms
from articles.models import Article


class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ["title", "content"]

    def clean_title(self):
        # after the form submission clean_data method is available
        cleaned_data = self.cleaned_data
        # print(cleaned_data)
        title = cleaned_data.get("title")
        title_taken = Article.objects.filter(title__exact=title).first()
        if title_taken:
            raise forms.ValidationError("This title is taken")
        return title

    # def clean_content(self):
    #     cleaned_data = self.cleaned_data
    #     # print(cleaned_data)
    #     return cleaned_data

    def clean(self):
        cleaned_data = self.cleaned_data #this is a dictionary
        # print(clean_data)
        # print(clean_data.get("title"))
        # print(clean_data.get("content"))
        return cleaned_data