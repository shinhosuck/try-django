from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article
from articles.forms import CreateArticleForm, ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q




def home(request):
    articles = Article.objects.all()
    context={"articles": articles}
    return render(request, "articles/home.html", context=context)


def detail(request, slug):
    try:
        article = Article.objects.get(slug=slug)
        print(article.get_absolute_url())
    except Exception as e:
        error = e
        messages.error(request, f"{error}")
        return redirect("articles:home")
    except Article.DoesNotExist:
        raise Http404
    context = {"article": article}
    return render(request, "articles/detail.html", context=context)


def search_view(request):
    # print(request)
    # print(dir(request))
    # print(request.GET) this is dictionary
    query = request.GET.get("q")
    title2 =  Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    title = Article.objects.filter(title__icontains=query)
    context = {"article": title}
    return render(request, "articles/search.html", context)

@login_required
def create_article_view(request):
    form = CreateArticleForm()
    context= {
        "form": form
    }
    if request.method == "POST":
        form = CreateArticleForm(request.POST)
        author = request.user
        context["form"] = form
        if form.is_valid():
            # when using built in form, do not have to user "clean_data" built in method.
            # title = form.cleaned_data.get("title")
            # content = form.cleaned_data.get("content")
            title = request.POST.get("title")
            content = request.POST.get("content")
            article = Article.objects.create(author=author, title=title, content=content)
            # context = {"article": article}
            return redirect("articles:article-detail",  article.slug)
    return render(request, "articles/create.html", context)
    # if not request.user.is_authenticated:
    #     messages.warning(request, "You are not logged in!")
    #     return render(request, "users/login.html", context=None)
    # form = CreateArticleForm(request.POST, None)
    # if form.is_valid():
        # this can be called after .is_valid()#
        # cleaned = form.cleaned_data.get("title")
        # cleaned = form.cleaned_data.get("content")
        # print(cleaned)
    # if request.method == "POST":
    #     if request.user.is_authenticated:
    #         author = request.user
    #         # redirect_url = request.POST.get("next")
    #         form = CreateArticleForm(request.POST)
    #         if form.is_valid():
    #             article = form.save(commit=False)
    #             article.author = author
    #             # article.save()
    #             messages.success(request, "Article has been successfully created.")
    #             return render(request, "articles/detail.html", context={"article": article})
    #         else:
    #             messages.warning(request, "Try again! There was an error during submission.")
    #             return redirect("articles:article-new")
    #     messages.warning(request, "You are not logged in!")
    #     return render(request, "users/login.html", context=None)
    # return render(request, "articles/article_form.html", context=None)


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

@login_required
def edit_article_view(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    context = {
        "form": form
    }
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        context["form"] = form
        if form.is_valid():
            article = form.save()
            context = {
                "article": article
            }
            return render(request, "articles/detail.html", context)
    return render(request, "articles/create.html", context)