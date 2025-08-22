from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserRegistration


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.'
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUserRegistration
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserRegistration
        fields = ("username", "email")


class UserShippingForm(forms.ModelForm):
    class Meta:
        model = CustomUserRegistration
        fields = ['firstname', 'lastname', 'phone_number', 'province', 'city', 'address', 'postal_code', 'extrainfo']
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'province': forms.TextInput(attrs={'placeholder': 'Province'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Address'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code'}),
            'extrainfo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Extra Info'}),
        }
ProfileEditForm = UserShippingForm
