from django import forms
from .models import Sticker
from accounts.models import Profile


class StickerForm(forms.ModelForm):
    class Meta:
        model = Sticker
        fields = ['name', 'description', 'price', 'image', 'tags', 'stock', 'is_active', 'category']


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'phone', 'province', 'city', 'address', 'postal_code', 'extrainfo']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'province': forms.TextInput(attrs={'placeholder': 'Province'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Address'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code'}),
            'extrainfo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Extra Info'}),
        }