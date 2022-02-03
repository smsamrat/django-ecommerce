from atexit import register
from django import template
from cart.models import Cart, order

register = template.Library()

@register.filter
def cart_view(user):
    cart = Cart.objects.filter(user=user, purchased=False)
    if cart.exists():
        return cart
    else:
        return cart
    
@register.filter
def total_cart_price(user):
    total_cart= order.objects.filter(user=user, ordered=False)
    if total_cart.exists():
        return total_cart[0].order_item_total()
    else:
        return 0
    
@register.filter
def cart_count(user):
    total_cart= order.objects.filter(user=user, ordered=False)
    if total_cart.exists():
        return total_cart[0].orders_item.count()
    else:
        return 0