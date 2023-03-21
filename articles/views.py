from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article
from articles.forms import CreateArticleForm
from django.contrib import messages


def home(request):
    articles = Article.objects.all()
    article = Article.objects.get(pk=1)
    article_filter = Article.objects.filter(title="Title 2").first()
    article.title = "Title 1"
    article.save()
    # print(article_filter)
    context={
        "articles": articles
    }
    '''
    ======================
    THIS IS RARELY USED!!!
    ======================
    template = get_template("home.html")
    html = template.render(context)
    '''
    html = render_to_string("articles/home.html", context)
    return HttpResponse(html)


def detail(request, id=None):
    article = None
    if id:
        article = Article.objects.get(id=id)
    context = {
        "article": article
    }
    data = render_to_string("articles/detail.html", context=context)
    return HttpResponse(data)

def contact_view(request):
    return render(request, "articles/contact.html", context=None)

def search_view(request):
    # print(request)
    # print(dir(request))
    # print(request.GET) this is dictionary
    query = request.GET.get("q")
    title = Article.objects.filter(title__icontains=query)
    # content = Article.objects.filter(content__icontains=query)
    # print(title)
    context = {
        "article": title
    }
    return render(request, "articles/search.html", context)


def new_article_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            author = request.user
            # redirect_url = request.POST.get("next")
            form = CreateArticleForm(request.POST, None)
            if form.is_valid():
                article = form.save()
                article.author = author
                article.save()
                messages.success(request, "Article has been successfully created.")
                # return redirect(f"/article/{new_article.id}")
                return render(request, "articles/detail.html", context={"article": article})
            else:
                messages.warning(request, "Try again! There was an error during submission.")
                return redirect("articles:article-new")
        messages.warning(request, "You are not logged in!")
        return render(request, "articles/article_form.html", context=None)
    return render(request, "articles/article_form.html", context=None)


"""
THIS IS A LONG WAY WITHOUT USING BUILT IN FORM
"""
# def new_article_view(request):
#     context = {}
#     if request.method == "POST":
#         if request.POST.get("title") and request.POST.get("content"):
#             title = request.POST.get("title")
#             content = request.POST.get("content")
#             article = Article.objects.create(author=request.user, 
#                             title=title, content=content)
#             context["article"] = article
#     return render(request, "articles/article_form.html", context=context)
