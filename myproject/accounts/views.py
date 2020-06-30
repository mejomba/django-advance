from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from .mixins import (
	FormRenderMixin,
	FormValidMixin,
	AuthorAccessMixin,
	SuperUserAccessMixin,
)


class AccountView(LoginRequiredMixin, ListView):
	template_name = 'registration/home.html'

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all().order_by('-publish')
		else:
			return Article.objects.filter(author=self.request.user).order_by('-publish')


class CreateArticle(LoginRequiredMixin ,FormRenderMixin ,FormValidMixin, CreateView):
	model = Article
	template_name = 'registration/create-update-article.html'

	# fields = ['author', 'title', 'slug', 'description', 'thumbnail', 'publish', 'status', 'category',]


class UpdateArticle(LoginRequiredMixin ,AuthorAccessMixin ,FormRenderMixin ,FormValidMixin, UpdateView):
	model = Article
	template_name = 'registration/create-update-article.html'


class DeleteArticle(SuperUserAccessMixin, DeleteView):
	model = Article
	success_url = reverse_lazy('accounts:account')
	template_name = 'registration/confirm-delete-article.html'