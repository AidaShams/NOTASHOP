from django import forms
from .models import Sticker

class StickerForm(forms.ModelForm):
    class Meta:
        model = Sticker
        fields = [
            'name', 'description', 'price', 'tags', 'stock', 'is_active', 'category'
        ]