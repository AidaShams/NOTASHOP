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

    def decrement(self, sticker):
        sticker_id = str(sticker.id)
        if sticker_id in self.cart:
            self.cart[sticker_id]['quantity'] -= 1
            if self.cart[sticker_id]['quantity'] <= 0:
                self.remove(sticker)
            else:
                self.save()

    def __iter__(self):     #iter makes a copy of the item
        sticker_ids = self.cart.keys()
        stickers = Sticker.objects.filter(id__in=sticker_ids)

        for sticker in stickers:
            cart_item = self.cart[str(sticker.id)]
            cart_item_copy = cart_item.copy()
            cart_item_copy['sticker'] = sticker
            cart_item_copy['price'] = Decimal(cart_item['price'])
            cart_item_copy['total_price'] = cart_item_copy['price'] * cart_item_copy['quantity']
            yield cart_item_copy

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()