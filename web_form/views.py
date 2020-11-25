from django.shortcuts import render
from django.http import HttpResponse, Http404

from .forms import ArticleForm
from .models import Article


def list_articles_view(request):
    articles_qs = Article.objects.all()
    return render(request, 'web_form/list.html', {'list': articles_qs})


def article_create(request):
    form = ArticleForm(request.POST or None)
    reset = False

    if request.method == "POST":
        if form.is_valid():
            #form.save()
            return HttpResponse(f"Сообщение {form['user_name'].value()} отправленно!")
        reset = True

    return render(request, 'web_form/create.html', {'form': form, 'reset': reset})


def article_view(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найденна!")

    return render(request, 'web_form/form.html', {'form': article})
