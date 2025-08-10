from django.urls import path
from .views import HomeView, StickerListView, StickerDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('stickers/', StickerListView.as_view(), name='sticker_list'),
    path('stickers/<slug:slug>/', StickerDetailView.as_view(), name='sticker_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]


#did the path with slugs instead of int:pk (making it more user-friendly)

#TODO: make article app and import the views from there
# i mean create/delete/detail/update