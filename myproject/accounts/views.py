from django.shortcuts import render
from django.views.generic import ListView, CreateView


from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article

class AccountView(LoginRequiredMixin, ListView):
	template_name = 'registration/home.html'

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all().order_by('-publish')
		else:
			return Article.objects.filter(author=self.request.user).order_by('-publish')


class CreateArticle(LoginRequiredMixin ,CreateView):
	model = Article
	template_name = 'registration/create-update-article.html'

	fields = ['author', 'title', 'slug', 'description', 'thumbnail', 'publish', 'status', 'category',]

