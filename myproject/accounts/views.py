from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
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
	AuthorsAccessMixin,
	SuperUserAccessMixin,
)
from .models import User
from .forms import ProfileForm


class AccountView(LoginRequiredMixin, AuthorsAccessMixin, ListView):
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


class Profile(LoginRequiredMixin ,UpdateView):
	model = User
	template_name = 'registration/profile.html'
	form_class = ProfileForm
	success_url = reverse_lazy('accounts:profile')

	def get_object(self):
		return User.objects.get(pk=self.request.user.pk)

	def get_form_kwargs(self):
		kwargs = super(Profile, self).get_form_kwargs()
		kwargs.update({
			'user': self.request.user
			})
		return kwargs


class Login(LoginView):
	def get_success_url(self):
		if self.request.user.is_superuser or self.request.user.is_author:
			return reverse_lazy('accounts:account')
		else:
			return reverse_lazy('accounts:profile')