from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<slug:slug>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', ArticleDeleteView.as_view(), name='delete'),
]