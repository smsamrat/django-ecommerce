from msilib.schema import Class
from re import template
from django.http import request
from django.shortcuts import render
from django.template import context
from django.views.generic import ListView,DetailView, TemplateView
from store.models import Product, ProductImages, BannerImage

class ProductListView(TemplateView):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        bannerimage = BannerImage.objects.filter(is_active=True).order_by('-id')
        context = {
            'products':products,
            'bannerimage':bannerimage,
        }
        return render(request, 'store/index.html',context)

    def post(self, request, *args, **kwargs):
            if request.method == 'post' or request.method == 'POST':
                product_search = request.POST.get('product_search')
                products = Product.objects.filter(name__icontains=product_search).order_by('-id')
                context = {
                    'products':products
                }
                return render(request, 'store/index.html',context)

                
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
        

