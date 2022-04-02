from django.shortcuts import render
from .models import Article, Tag


def articleList(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    if request.method=="POST":
        obj = request.POST.get('filter')
        try:
            tag = Tag.objects.get(name=obj)
            articles = Article.objects.filter(tags__name = tag.name)
        except Exception as E:
            print(str(E))
            pass

    params = {
        'articles':articles,
        'tags':tags

    }
    return render(request , 'article/list.html', params)

def article(request,pk):
    article = Article.objects.filter(id=pk)
    article = article[0]
    paras = article.text.split('|')

    params = {
        'article':article,
        'paras': paras
    }

    # return render(request , 'article/article.html',params)
    return render(request , 'index-2.html', params)