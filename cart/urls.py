
from django.urls import path
from cart import views


urlpatterns = [
    path('cart/add-to-cart/<int:pk>/',views.add_to_cart, name='add-to-cart')
]
