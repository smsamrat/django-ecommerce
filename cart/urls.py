
from django.urls import path
from cart import views


urlpatterns = [
    path('cart/add-to-cart/<int:pk>/',views.add_to_cart, name='add-to-cart'),
    path('cart-view/',views.cartView, name='cart'),
    path('cart-remove/<int:pk>/',views.cart_item_remove, name="remove-cart"),
    path('cart-item-increase/<int:pk>/',views.cart_item_increase, name='cart-item-increase'),
    path('cart-item-decrease/<int:pk>/',views.cart_item_decrease, name='cart-item-decrease'),
]
