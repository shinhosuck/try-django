from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

# from articles.admin import ArticleAdmin
from articles.models import Article
from articles.forms import ArticleForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    articles = Article.objects.all()
    # article = get_object_or_404(Article, pk=1)
    # article.title = 'updated title'
    # article.save()
    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)

# def home(request):
#     post = Article.objects.get(id=1)
#     context = {
#         'title': post.title,
#         'content': post.content
#     }
#     django_template = render_to_string('home.html', context=context)
#     return HttpResponse(django_template)

def about(request):
    return render(request, 'about.html', {})


def search(request):
    searched = request.GET # this is a dictionary
    parsed_dict = searched.get('q')
    print(parsed_dict)
    article = None
    
    try:
        article = Article.objects.filter(title = parsed_dict).first()
    except:
        pass
    print(article)
    if article:
        context = {
            'article': article
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html', {})


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    content = article.content
    context = {
        'article': article.title, 
        'content': content
    }
    return render(request, 'article_detail.html', context)


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            # ---WHEN USING form.ModelForm ALL YOU NEED TO DO IS save()
            new_article = form.save()

            #---- IF USING form.Form USE THIS-------
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # new_article = Article()
            # new_article.title = title
            # new_article.content = content
            # new_article.save()
            context = {
                'new_article': new_article
            }
            return render(request, 'create.html', context)
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     new_article = Article.objects.create(title=title, content=content)
    #     return render(request, 'create.html', {'new_article': new_article})
    
    form = ArticleForm()
    # print(dir(article_form))
    context = {
        'form': form
    }
    return render(request, 'create.html', context)



def user_register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('articles:user-login')
    else:
        context = {
                'form': form
            }
        return render(request, 'users/register.html', context)


def user_login(request):
    # user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            context = {}
            context['error'] = 'There was a problem with your username or password'
            return render(request, 'users/login.html', context)
        else:
            login(request, user)
            return redirect('articles:home')
    return render(request, 'users/login.html', {})


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('articles:user-login')
    else:
        return render(request, 'users/logout.html', {})