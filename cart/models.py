from django.db import models
from django.contrib.auth.models import User
from store.models import Product, Product_variationValue

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    cart_item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.cart_item}"
    
    def get_cart_item_total(self):
        total =  self.cart_item.price * self.quantity
        float_total = format(total,'0.2f')
        return float_total
    
    def variation_single_price(self):
        sizes = Product_variationValue.objects.filter(variation='size', product=self.cart_item)
        colors = Product_variationValue.objects.filter(variation='color', product=self.cart_item)
        for size in sizes:
            if colors.exists():
                for color in colors:
                    if color.name == self.color:
                        c_price = color.price
                if size.name == self.size:
                    total = size.price + c_price
                    net_price = total
                    float_total = format(net_price, '0.2f')
                    return float_total
            else:
                if size.name == self.size:
                    total = size.price
                    float_total = format(total, '0.2f')
                    return float_total

    def variation_total(self):
        sizes = Product_variationValue.objects.filter(variation='size', product=self.cart_item)
        colors = Product_variationValue.objects.filter(variation='color', product=self.cart_item)
        for size in sizes:
            if colors.exists():
                for color in colors:
                    if color.name == self.color:
                        c_price = color.price
                        total_quantity_price = c_price * self.quantity
                if size.name == self.size:
                    total = size.price * self.quantity
                    net_total = total + total_quantity_price
                    float_total = format(net_total, '0.2f')
                    return float_total
            else:
                if size.name == self.size:
                    total = size.price * self.quantity
                    float_total = format(total, '0.2f')
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
            total += float(total_order_items.get_cart_item_total())
        return total
    