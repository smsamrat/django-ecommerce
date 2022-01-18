from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    cart_item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.cart_item}"
    
    def get_cart_item_total(self):
        total =  self.cart_item.price * self.quantity
        float_total = float(total,'0.2f')
        return float_total
    
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    orders_item = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=225, blank=True, null=True)
    orderId = models.CharField(max_length=225, blank=True, null=True)
    
    def order_item_total(self):
        total = 0
        for total_order_items in self.orders_item.all():
            total = float(total_order_items.get_cart_item_total)
        return total
    