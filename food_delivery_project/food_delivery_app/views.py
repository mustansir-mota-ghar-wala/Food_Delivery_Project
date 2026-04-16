from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.template.defaultfilters import first
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Restaurant,Food_Items
# Create your views here

def Register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'username already taken')
            return redirect('register')

        user = User.objects.create(
            first_name = name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.success(request,'account created successfully')
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
    return render(request,'home.html')

def Logout(request):
    logout(request)
    return redirect('/login')

def Food_items(request,id):
    restaurant = Restaurant.objects.get(id=id)
    food_itmes = Food_Items.objects.filter(restaurant=restaurant)
    context = {'food_item':food_itmes, 'restaurant': restaurant}
    return render(request,'food_items.html',context)