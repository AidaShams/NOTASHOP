from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegister
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', UserRegister.as_view(), name='signup'),
]