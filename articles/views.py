from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article


def home(request):
    articles = Article.objects.all()
    article = Article.objects.get(pk=1)
    article_filter = Article.objects.filter(title="Title 2").first()
    article.title = "Title 1"
    article.save()
    print(article_filter)
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
    html = render_to_string("home.html", context)
    return HttpResponse(html)


def detail(request, id=None):
    article = None
    if id:
        article = Article.objects.get(id=id)
    context = {
        "article": article
    }
    data = render_to_string("detail.html", context=context)
    return HttpResponse(data)

def contact_view(request):
    return render(request, "contact.html", context=None)

def search_view(request):
    # print(request)
    # print(dir(request))
    # print(request.GET) this is dictionary
    query = request.GET.get("q")
    title = Article.objects.filter(title__icontains=query)
    # content = Article.objects.filter(content__icontains=query)
    print(title)
    context = {
        "article": title
    }
    return render(request, "search.html", context)