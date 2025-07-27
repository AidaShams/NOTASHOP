from django.shortcuts import render, get_object_or_404
from .models import Sticker, Category
# Create your views here.
def home(request):
    return render(request, 'home.html')

def sticker_list(request):
    stickers = Sticker.objects.filter(is_active=True)
    return render(request, 'store/sticker_list.html', {'stickers': stickers})

def sticker_detail(request, slug):
    sticker = get_object_or_404(Sticker, slug=slug, is_active=True)
    return render(request, 'store/sticker_detail.html', {'sticker': sticker})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    stickers = Sticker.objects.filter(category=category, is_active=True)
    return render(request, 'store/category_detail.html', {'category': category, 'stickers': stickers})