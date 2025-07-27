from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('sticker/<int:pk>/', views.sticker_detail, name='sticker_detail'),
]