from django.http import request
from django.shortcuts import render
from django.template import context
from django.views.generic import ListView,DetailView
from store.models import Product, ProductImages, BannerImage


class ProductListView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bannerimage']= BannerImage.objects.filter(is_active=True).order_by('-id')
        return context
    

class Product_Details(DetailView):
    model = Product
    template_name= 'store/product.html'
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images']=ProductImages.objects.filter(product=self.object.id)
        return context
    

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['product_images']=ProductImages.objects.filtter(product=self.objects.id)
    #     return context
    
    
# def ProductDetails(request, pk):
#     item = Product.objects.get(id=pk)
#     context={
#         'item':item
#     }
    
#     return render(request,'store/product.html', context)
        

