from django.shortcuts import render, get_object_or_404, redirect
from django.template import context
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
        
            
def cartView(request):
    carts = Cart.objects.filter(user=request.user, purchased=False) 
    orders = order.objects.filter(user=request.user, ordered=False) 
    if carts.exists() and orders.exists():
        ordered = orders[0]
        context ={
            'carts':carts,
            'ordered':ordered
        }
    return render(request, 'store/cart.html',context)

def cart_item_remove(request, pk):
    item = get_object_or_404(Product, pk=pk)
    orders = order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        ordered = orders[0]
        if ordered.orders_item.filter(cart_item=item).exists():
            order_item = Cart.objects.filter(cart_item=item, user=request.user, purchased=False)[0]
            ordered.orders_item.remove(order_item)
            order_item.delete()
            return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('cart')


def cart_item_increase(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qus = order.objects.filter(user=request.user, ordered=False)
    if order_qus.exists():
        ordered = order_qus[0]
        if ordered.orders_item.filter(cart_item=item).exists():
            order_item = Cart.objects.filter(cart_item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >=1:
                order_item.quantity += 1
                order_item.save()
                return redirect('cart')
            else:
                return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('index')


def cart_item_decrease(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qus = order.objects.filter(user=request.user, ordered=False)
    if order_qus.exists():
        ordered = order_qus[0]
        if ordered.orders_item.filter(cart_item=item).exists():
            order_item = Cart.objects.filter(cart_item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect('cart')
            else:
                ordered.orders_item.remove(order_item)
                order_item.delete()
                return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('index')




