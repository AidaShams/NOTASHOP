from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    approve_comment

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('update/<slug:slug>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', ArticleDeleteView.as_view(), name='delete'),
    path('approve-comment/<int:comment_id>/', approve_comment, name='admin-approve-comment'),
]
