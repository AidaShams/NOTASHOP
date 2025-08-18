from .models import Category
from .cart import Cart

#this function is supposed to make the menu hold the menu items
def categories_processor(request):
    return {'categories': Category.objects.all()}

def cart(request):
    return {'cart': Cart(request)}

# TODO: look up this code see what's wrong