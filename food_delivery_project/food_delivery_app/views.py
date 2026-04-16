from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.template.defaultfilters import first
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Restaurant
# Create your views here

def Register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name = name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'account created successfully')
        return redirect('/login')
    return render(request,'register.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request,"username not valid, Register yourself")
            return redirect('/register')
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/home')
    return render(request,'login.html')

@login_required(login_url='login')
def Home(request):
    restaurants = Restaurant.objects.all()
    return render(request,'home.html',{'restaurants': restaurants})

def Logout(request):
    logout(request)
    return redirect('/login')
