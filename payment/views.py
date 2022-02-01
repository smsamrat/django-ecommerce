
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from payment.models import BillingAddress
from payment.forms import BillingAddressForm
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
        total_price_after_discount = order_qs[0].total_price_after_discount()



        context = {
            'billing_address':form,
            'order_item':order_item,
            'order_totals':order_totals,
            'total_price_after_discount':total_price_after_discount,
        }
        return render(request, 'store/checkout.html',context)





