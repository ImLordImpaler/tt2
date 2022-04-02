from django.shortcuts import render, redirect
from .models import Article, Tag ,Comment



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

def newComment(request,pk):
    if request.method=='POST':
        text = request.POST.get('comment')
        art = Article.objects.get(id=pk)
        comment = Comment.objects.create(body=text , article = art)
        comment.save()
        art.comments.add(comment)
        art.save()
    return redirect('article', pk=pk)