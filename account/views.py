
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



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

