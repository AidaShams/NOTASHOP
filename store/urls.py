from django.urls import path
from .views import HomeView, StickerListView, StickerDetailView, CategoryListView, CategoryDetailView, sticker_create, \
    cart_add, cart_remove, cart_detail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('stickers/', StickerListView.as_view(), name='sticker_list'),
    path('stickers/create/', sticker_create, name='sticker_create'),
    path('stickers/<slug:slug>/', StickerDetailView.as_view(), name='sticker_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:sticker_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:sticker_id>/', cart_remove, name='cart_remove'),
]

# did the path with slugs instead of int:pk (making it more user-friendly)

# TODO: make article app and import the views from there
# i mean create/delete/detail/update
