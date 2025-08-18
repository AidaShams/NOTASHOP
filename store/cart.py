from decimal import Decimal
from django.conf import settings
from .models import Sticker


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, sticker, quantity=1, update_quantity=False):
        sticker_id = str(sticker.id)
        if sticker_id not in self.cart:
            self.cart[sticker_id] = {'quantity': 0, 'price': str(sticker.price)}
        if update_quantity:
            self.cart[sticker_id]['quantity'] = quantity
        else:
            self.cart[sticker_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, sticker):
        sticker_id = str(sticker.id)
        if sticker_id in self.cart:
            del self.cart[sticker_id]
            self.save()

    def __iter__(self):
        sticker_ids = self.cart.keys()
        stickers = Sticker.objects.filter(id__in=sticker_ids)
        for sticker in stickers:
            item = self.cart[str(sticker.id)]
            item['sticker'] = sticker
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()