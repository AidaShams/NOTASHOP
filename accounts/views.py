from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CustomUserRegistrationForm, UserShippingForm
from store.cart import Cart
from store.models import Sticker


class UserRegister(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return redirect(self.get_success_url())


@login_required
def profile_view(request):
    user = request.user
    edit_mode = request.GET.get('edit') == '1'

    if request.method == 'POST':
        form = UserShippingForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserShippingForm(instance=user)

    context = {
        'user': user,
        'form': form,
        'edit_mode': edit_mode
    }
    return render(request, 'account/profile.html', context)


@login_required
def checkout_view(request):
    cart = Cart(request)
    items = []
    for item in cart:
        items.append({
            'sticker': item.sticker,
            'quantity': item.quantity,
            'total_price': item.total_price
        })

    context = {
        'user': request.user,
        'items': items,
        'total_price': cart.get_total_price()
    }
    return render(request, 'account/checkout.html', context)
