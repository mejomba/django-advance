from django.urls import path
from blog.views import detail, category, ListArticle


app_name = 'blog'
urlpatterns = [
    path('', ListArticle.as_view(), name='home'),
    path('page/<int:page>/', ListArticle.as_view(), name='home'),
    path('article/<slug:slug>/', detail, name='detail'),
    path('category/<slug:slug>/', category, name='category'),
    path('category/<slug:slug>/page/<int:page>/', category, name='category'),
]