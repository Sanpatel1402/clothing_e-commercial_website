from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart, CartItem
# Create your views here.


def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def review_cart(request, total=0, total_price=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        total_price = total
        tax = (18 * total_price) / 100
        grand_total = total_price + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total_price': total_price,
        'quantity': quantity,
        'tax': tax,
        'grand_total': grand_total,
        'cart_items': cart_items
    }
    return render(request, 'place_order.html', context)


def order(request, total=0, total_price=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        total_price = total
        tax = (18 * total_price) / 100
        grand_total = total_price + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total_price': total_price,
        'quantity': quantity,
        'tax': tax,
        'grand_total': grand_total,
        'cart_items': cart_items
    }
    return render(request, 'order_complete.html', context)