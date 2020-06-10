from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article

def home(request):
	context = {
			'articles': Article.objects.all()
	}
	return render(request, 'blog/home.html', context)


def detail(request, slug):
	context = {
			'article': Article.objects.get(slug=slug)
	}
	return render(request, 'blog/detail.html', context)
