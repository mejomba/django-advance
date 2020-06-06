from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
	return HttpResponse('hello from view')

def api(request):
	data = {"message": 'hello'}
	return JsonResponse(data, status=200)