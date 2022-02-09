
from urllib import request
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from cart.models import Cart, order
from account.models import Profile
from payment.models import BillingAddress



# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return HttpResponse("is_authencate")
    else:
        form = RegistrationForm()
        if request.method == 'POST' or request.method == 'post':  
            form = RegistrationForm(request.POST) 
            if form.is_valid():
                form.save()  
                return HttpResponse('Account created successfully') 
        
        context={
            'form':form
        }
        
    return render(request,'register.html',context)

def loginForm(request):
    if request.user.is_authenticated:
        return HttpResponse('logined In')
    else:
        if request.method == 'POST' or request.method == 'post':
            username=request.POST.get('username')
            password=request.POST.get('password')
            customer=authenticate(request,username=username,password=password)
            if customer is not None:
                login(request, customer)
                return HttpResponse('login successfull')
            else:
                return HttpResponse('404')
                
    return render(request,'login.html')

# Profile information
class ProfileInfo(TemplateView):
    def get(self, request, *args, **kwargs):
        products = order.objects.filter(user=request.user, ordered=True)
        cart_products = Cart.objects.filter(user=request.user, purchased=True)
        context ={
            'products':products,
            'cart_products':cart_products
        }
        return render(request, 'profile.html',context)

    def post(self, request, *args, **kwargs):
        pass

    # def profileView(request,pk):
    #     item= get_