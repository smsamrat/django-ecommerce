
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from payment.forms import PaymentMethod
from cart.models import Cart, order

from django.views.generic import TemplateView

class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        save_address = BillingAddress.objects.get_or_create(user = request.user or None)
        save_address = save_address[0]
        form = BillingAddressForm(instance=save_address)

        order_qs = order.objects.filter(user = request.user, ordered=False)
        order_item = order_qs[0].orders_item.all()
        order_totals = order_qs[0].order_item_total()

        payment_method = PaymentMethod()


        context = {
            'billing_address':form,
            'order_item':order_item,
            'order_totals':order_totals,
            'payment_method':payment_method
        }
        return render(request, 'store/checkout.html',context)

    def post(self, request, *args, **kwargs):
        save_address = BillingAddress.objects.get_or_create(user = request.user or None)
        save_address =save_address[0]
        form = BillingAddressForm(instance=save_address)
        payment_obj = order.objects.filter(user = request.user, ordered=False)[0]
        payment_form = PaymentMethod(instance=payment_obj)
        if request.method == 'post' or request.method == 'POST':
            form = BillingAddressForm(request.POST, instance=save_address)
            pay_form = PaymentMethod(request.POST, instance=payment_obj)
            if form.is_valid() and pay_form.is_valid():
                form.save()
                pay_method = pay_form.save()

                if not save_address.is_fully_filled():
                    print('it is working')
                    return redirect('checkout')

                # cash on delivery process
                if pay_method.payment_method == "Cash on Delivery":
                    order_qs = order.objects.filter(user=request.user, ordered=False)
                    orders = order_qs[0]
                    orders.ordered = True
                    orders.orderId = orders.id
                    orders.paymentId = pay_method.payment_method
                    orders.save()
                    cart_items = Cart.objects.filter(user=request.user, purchased=False)
                    for item in cart_items:
                        item.purchased = True
                        item.save()
                    return redirect('index')



            






