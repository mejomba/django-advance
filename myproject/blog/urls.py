from django.urls import path
from blog.views import ListArticle, DetailArticle, CategoryList, AuthorList



app_name = 'blog'
urlpatterns = [
    path('', ListArticle.as_view(), name='home'),
    path('page/<int:page>/', ListArticle.as_view(), name='home'),
    path('article/<slug:slug>/', DetailArticle.as_view(), name='detail'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>/', CategoryList.as_view(), name='category'),
    path('author/<slug:username>/', AuthorList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>/', AuthorList.as_view(), name='author'),
]