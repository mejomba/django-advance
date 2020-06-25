from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.mixin import LoginRequiredMixin

class ArticleList(LoginRequiredMixin, ListView):
	queryset = Article.objects.all()
	template_name = 'accounts/home.html'