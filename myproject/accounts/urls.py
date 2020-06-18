from django.urls import path
from blog.views import ArticleList



app_name = 'accounts'
urlpatterns = [
	path('login/', ArticleList.as_view(), name='login')   
]