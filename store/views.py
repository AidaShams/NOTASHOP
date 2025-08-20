from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Sticker, Category
from .forms import StickerForm
from .cart import Cart
from .forms import CartAddForm
from django.http import JsonResponse


class HomeView(TemplateView):
    template_name = "home.html"


class StickerListView(ListView):
    model = Sticker
    template_name = "store/sticker_list.html"
    context_object_name = "stickers"

    def get_queryset(self):
        return Sticker.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        for sticker in context["stickers"]:
            sticker.cart_quantity = cart.cart.get(str(sticker.id), {}).get("quantity", 0)
        return context


class StickerDetailView(DetailView):
    model = Sticker
    template_name = "store/sticker_detail.html"
    context_object_name = "sticker"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Sticker.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = CartAddForm()
        return context


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
        context['stickers'] = Sticker.objects.filter(
            category=self.object,
            is_active=True
        )
        context["cart"] = Cart(self.request)
        return context


def cart_add(request, sticker_id):
    cart = Cart(request)
    sticker = get_object_or_404(Sticker, id=sticker_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            sticker=sticker,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({
            "success": True,
            "sticker_id": sticker.id,
            "quantity": cart.cart[str(sticker.id)]['quantity'],
            "cart_total": cart.get_total_price(),
            "cart_count": sum(item['quantity'] for item in cart.cart.values())
        })
    return redirect("cart_detail")


def cart_remove(request, sticker_id):
    cart = Cart(request)
    sticker = get_object_or_404(Sticker, id=sticker_id)
    cart.remove(sticker)
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({
            "success": True,
            "sticker_id": sticker.id,
            "cart_total": cart.get_total_price(),
            "cart_count": sum(item['quantity'] for item in cart.cart.values())
        })
    return redirect('cart_detail')


def cart_decrement(request, sticker_id):
    cart = Cart(request)
    sticker = get_object_or_404(Sticker, id=sticker_id)
    cart.decrement(sticker)
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        qty = cart.cart.get(str(sticker.id), {}).get('quantity', 0)
        return JsonResponse({
            "success": True,
            "sticker_id": sticker.id,
            "quantity": qty,
            "cart_total": cart.get_total_price(),
            "cart_count": sum(item['quantity'] for item in cart.cart.values())
        })
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddForm(
            initial={'quantity': item['quantity'], 'update': True}
        )
    return render(request, 'store/cart_detail.html', {'cart': cart})


# only admin can see create sticker menu
@user_passes_test(lambda u: u.is_superuser)
def sticker_create(request):
    if request.method == 'POST':
        form = StickerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sticker_list')
    else:
        form = StickerForm()
    return render(request, 'store/sticker_form.html', {'form': form})
