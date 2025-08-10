from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserRegistrationForm
# Create your views here.

class UserRegister(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return redirect(self.get_success_url())