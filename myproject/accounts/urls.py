from django.urls import path
from django.contrib.auth import views
from accounts.views import (
    AccountView,
    CreateArticle,
    UpdateArticle,
    DeleteArticle,
    Profile,
    Login,
)


app_name = 'accounts'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('', AccountView.as_view(), name='account'),
    path('article/create/', CreateArticle.as_view(), name='create-article'),
    path('article/update/<int:pk>', UpdateArticle.as_view(), name='update-article'),
    path('article/delete/<int:pk>', DeleteArticle.as_view(), name='delete-article'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]