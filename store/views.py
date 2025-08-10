from django.views.generic import TemplateView, ListView, DetailView
from .models import Sticker, Category

class HomeView(TemplateView):
    template_name = "home.html"

class StickerListView(ListView):
    model = Sticker
    template_name = "store/sticker_list.html"
    context_object_name = "stickers"

    def get_queryset(self):
        return Sticker.objects.filter(is_active=True)

class StickerDetailView(DetailView):
    model = Sticker
    template_name = "store/sticker_detail.html"
    context_object_name = "sticker"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Sticker.objects.filter(is_active=True)

class CategoryListView(ListView):
    model = Category
    template_name = "store/category_list.html"
    context_object_name = "categories"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "store/category_detail.html"
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stickers'] = Sticker.objects.filter(category=self.object, is_active=True)
        return context