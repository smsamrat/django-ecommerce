from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from cart.models import Cart, order

# Create your views here.

def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    cart_order_item = Cart.objects.get_or_create(cart_item=item, user=request.user, purchased=False)
    order_qs = order.objects.filter(user=request.user, ordered=False)
    
    
    if order_qs.exists():
        orders = order_qs[0]
        if orders.orders_item.filter(cart_item=item).exists():
            color = request.POST.get('color')
            size = request.POST.get('size')
            quantity = request.POST.get('quantity')
            if quantity:
                cart_order_item[0].quantity += int(quantity)
            else:
                cart_order_item[0].quantity += 1
            cart_order_item[0].color = color
            cart_order_item[0].size = size
            cart_order_item[0].save()
            return redirect('index')
        else:
            color = request.POST.get('color')
            size = request.POST.get('size')
            cart_order_item[0].color = color
            cart_order_item[0].size = size
            orders.orders_item.add(cart_order_item[0])
            return redirect('index')
    else:
        orders = order(user=request.user)
        orders.save()
        orders.orders_item.add(cart_order_item[0])
        return redirect('index')
        
            
    
