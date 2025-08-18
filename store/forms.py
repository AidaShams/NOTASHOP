from django import forms
from .models import Sticker

class StickerForm(forms.ModelForm):
    class Meta:
        model = Sticker
        fields = [
            'name', 'description', 'price', 'tags', 'stock', 'is_active', 'category'
        ]

class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)