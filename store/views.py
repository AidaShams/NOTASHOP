from django.shortcuts import render, get_object_or_404
from .models import Sticker, Category
# Create your views here.

def home(request):
    stickers = Sticker.objects.all()
    return render(request, 'home.html', {'stickers': stickers})

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    stickers = Sticker.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'stickers': stickers})

def sticker_detail(request, pk):
    sticker = get_object_or_404(Sticker, pk=pk)
    return render(request, 'sticker_detail.html', {'sticker': sticker})