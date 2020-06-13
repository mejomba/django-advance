from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category

# def home(request, page=1):
# 	article_list = Article.objects.published()
# 	paginator = Paginator(article_list, 3)
# 	articles = paginator.get_page(page)
# 	context = {
# 			'articles': articles
# 	}
# 	return render(request, 'blog/home.html', context)

class ListArticle(ListView):
	# models = Article
	# template_name = 'blog/home.html'
	# context_object_name = "articles"
	queryset = Article.objects.published()
	paginate_by = 3

def detail(request, slug):
	context = {
			'article': get_object_or_404(Article.objects.published(), slug=slug)
	}
	return render(request, 'blog/detail.html', context)


def category(request, slug, page=1):
	category = get_object_or_404(Category, slug=slug, status=False)
	article_list = category.related_name.published()
	paginator = Paginator(article_list, 3)
	articles = paginator.get_page(page)
	context = {
		'category': category,
		'articles': articles
	}
	return render(request, 'blog/category.html', context)