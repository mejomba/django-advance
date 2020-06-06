from django.urls import path
from blog.views import home, api


app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('api/', api, name='api'),
]