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