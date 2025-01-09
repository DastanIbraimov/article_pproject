from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ArticleForm
from webapp.models import Article


def article_list_view(request):
    articles = Article.objects.order_by('-published_at')
    return render(request, "index.html", context={"articles": articles})


def article_create_view(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "create_article.html", {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author=form.cleaned_data['author'],
            )
            return redirect("article_detail", pk=article.pk)
        return render(request, "create_article.html", {'form': form})


def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", context={"article": article})


def article_update_view(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(initial={
            "title": article.title,
            "content": article.content,
            "author": article.author
        })
        return render(request, 'update_article.html', context={"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = get_object_or_404(Article, pk=pk)
            article.title = form.cleaned_data['title']
            article.content = form.cleaned_data['content']
            article.author = form.cleaned_data['author']
            article.save()
            return redirect("article_detail", pk=article.pk)
        else:
            return render(request, "update_article.html", {'form': form})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, "delete_article.html", context={"article": article})
    else:
        article.delete()
        return redirect("articles")
