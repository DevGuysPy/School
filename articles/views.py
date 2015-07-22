from django.shortcuts import render, redirect
from .models import Article

def article(request, article_id):
    ctx = {
        'article': Article.objects.get(id=article_id),
    }

    return render(request, 'article.html', ctx)

def new_article(request):
    if request.method == "POST":
        new_article_title = request.POST['title']
        new_article_text = request.POST['text']
        article = Article.objects.create(title=new_article_title, \
                                         text=new_article_text, author=request.user)
        return redirect('article_detail', article_id=article.id)
    return render(request, 'new_article.html')
