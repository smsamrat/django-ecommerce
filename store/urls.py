
from itertools import product
from unicodedata import name
from django.urls import path
from store import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('search', views.SearchProduct, name='search_product'),
    path('<slug:slug>', views.Product_Details.as_view(), name='product_details'),
]
