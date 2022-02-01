from ast import pattern
from typing import Pattern
from unicodedata import name
from django.urls import path
from payment import views

urlpatterns = [
    path ("checkout/",views.CheckoutTemplateView.as_view(), name='checkout')
]