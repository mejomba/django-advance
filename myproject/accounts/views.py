from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.mixin import loginrequiredMixin

class AccountView(ListView):
	queryset = Article.objects.all()
	template_name = 'accounts/home.html'
