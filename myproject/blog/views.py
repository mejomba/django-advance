from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
	context = {
			'title': 'my title',
			'body': 'my body',
	}
	return render(request, 'blog/home.html', context)

