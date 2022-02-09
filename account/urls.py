
from django.urls import path
from account import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginForm, name='loginForm'),
    path('profile/', views.ProfileInfo.as_view(), name='profile')
]
