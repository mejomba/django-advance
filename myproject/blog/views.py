from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article

def home(request):
	context = {
			'articles': get_list_or_404(Article, status='P')
	}
	return render(request, 'blog/home.html', context)


def detail(request, slug):
	context = {
			'article': get_object_or_404(Article, slug=slug, status='P')
	}
	return render(request, 'blog/detail.html', context)
