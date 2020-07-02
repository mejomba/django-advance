from django.http import Http404
from blog.models import Article
from django.shortcuts import get_object_or_404, redirect


class FormRenderMixin():

	def dispatch(self, request, *args, **kwargs):
		self.fields = ['title', 'slug', 'description', 'thumbnail', 'publish', 'status', 'is_special', 'category', 'optional_description']
		if request.user.is_superuser:
			self.fields.append('author')

		return super().dispatch(request, *args, **kwargs)


class FormValidMixin():

	def form_valid(self, form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit=False)
			self.obj.author = self.request.user
			if self.obj.status == 'I':
				self.obj.status = 'I'
			else:
				self.obj.status = 'D'

		return super().form_valid(form)


class AuthorAccessMixin():

	def dispatch(self, request, pk, *args, **kwargs):
		article = get_object_or_404(Article, pk=pk)
		if article.author == request.user and article.status in ['D', 'I', 'B'] or request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404


class AuthorsAccessMixin():

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_author or request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect('accounts:profile')


class SuperUserAccessMixin():

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404 ('شما اجازه دسترسی به این صفحه را ندارید')

		