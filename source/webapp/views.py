from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article


def article_list_view(request):
    articles = Article.objects.order_by('-published_at')
    return render(request, "index.html", context={"articles": articles})


def article_create_view(request):
    if request.method == "GET":
        return render(request, "create_article.html")
    else:
        article = Article.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            author=request.POST.get("author")
        )
        return redirect("article_detail", pk=article.pk)


def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", context={"article": article})


def article_update_view(request, pk):
    if request.method == "GET":
        return render(
            request, 'update_article.html',
            context={"article": get_object_or_404(Article, pk=pk)}
        )
    else:
        article = get_object_or_404(Article, pk=pk)
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.author = request.POST.get("author")
        article.save()
        return redirect("article_detail", pk=article.pk)


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("articles")
