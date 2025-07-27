from django.urls import path
from . import views

urlpatterns = [
    path('', views.sticker_list, name='sticker_list'),                      # /store/
    path('sticker/<slug:slug>/', views.sticker_detail, name='sticker_detail'), # /store/sticker/good-omens/
    path('categories/', views.category_list, name='category_list'),         # /store/categories/
    path('category/<slug:slug>/', views.category_detail, name='category_detail'), # /store/category/cute-stickers/

]