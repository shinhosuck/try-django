from django import forms
from articles.models import Article


class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = self.cleaned_data #this is a dictionary
        # print(cleaned_data)
        # print(clean_data.get("title"))
        # print(clean_data.get("content"))
        # title = cleaned_data.get("title")
        # content = cleaned_data.get("content")
        # taken_title = Article.objects.filter(title__exact=title).first()
        # print(dir(taken_title))
        # if taken_title:
        #     self.add_error("title", "This title is taken")
        # if len(content) > 500:
        #     self.add_error("content", "Content is too short")
        #     raise forms.ValidationError("Fix the error or errors to submit")
        return cleaned_data
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]

    def clean(self):
        data_cleaned = self.cleaned_data
        # title = data_cleaned.get("title")
        # content = data_cleaned.get("content")
        # title_taken = Article.objects.filter(title=title).first()
        # if title_taken:
        #     self.add_error("title", "This title is taken")
        # if len(content) > 500:
        #     self.add_error("content", "Content is too long")
        #     raise forms.ValidationError("Please fix the errors")
        return data_cleaned

