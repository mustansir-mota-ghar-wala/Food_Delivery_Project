from django.shortcuts import get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.template.defaultfilters import first
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Restaurant,Food_Items,Cart
from django.db.models import Sum
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


def Home(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request,'home.html',context)

def Logout(request):
    logout(request)
    return redirect('/login')

def Food_items(request,id):
    restaurant = Restaurant.objects.get(id=id)
    food_itmes = Food_Items.objects.filter(restaurant=restaurant)
    all_restaurants = Restaurant.objects.all()
    context = {
        'food_item':food_itmes, 
        'restaurant': restaurant,
        'all_restaurants': all_restaurants
    }
    return render(request,'food_items.html',context)

# @login_required(login_url='login')
# def cart(request,id):
#     user = request.user
#     food_item = get_object_or_404(Food_Items,id = id)

#     cart = request.session.get('cart',{})
#     id_str = str(food_item.id)

#     if id_str in cart :
#         cart[id_str]['quantity'] +=1
#     else :
#         cart[id_str] = {
#             "name": food_item.food_name,
#             "price": str(food_item.food_price),
#             "quantity": 1,
#             "restaurant": food_item.restaurant.name,
#             "user": user.username,
#         }
#         request.session['cart'] = cart
#     context = {'user':user}
#     return render(request,'cart.html',context)


@login_required(login_url='login')
def add_to_cart(request, id):
    # 1. Look up the food item the user clicked
    food_item = get_object_or_404(Food_Items, id=id)
    
    # 2. Add to database: If item exists, update; if not, create.
    # We use 'get_or_create' to avoid writing 10 lines of if/else logic.
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        food_item=food_item,
        defaults={'food_item_total': food_item.food_price}
    )
    
    if not created:
        # If it already was in the cart, increase quantity
        cart_item.food_item_quantity += 1
        cart_item.food_item_total = cart_item.food_item_quantity * food_item.food_price
        cart_item.save()
        
    return redirect('cart')
    
@login_required(login_url='login')
def cart(request):
    # 3. Fetch all items added by the current user
    cart_items = Cart.objects.filter(user=request.user)
    
    # 4. Calculate the Grand Total for the entire bill
    # 'aggregate' is a Django shortcut for doing math in the database
    grand_total = cart_items.aggregate(total=Sum('food_item_total'))['total'] or 0
    
    context = {
        'cart_items': cart_items,
        'grand_total': grand_total
    }
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def remove_cart_item(request, id):
    # 5. Find the cart entry and delete it
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required(login_url='login')
def decrease_quantity(request,id):
    cart_item = get_object_or_404(Cart,id=id,user=request.user)
    if cart_item.food_item_quantity > 1:
        cart_item.food_item_quantity -= 1
        cart_item.food_item_total = cart_item.food_item_quantity*cart_item.food_item.food_price
        cart_item.save()
        return redirect('cart')
    else :
        cart_item.delete()
    return redirect('cart')

@login_required(login_url='login')
def increase_quantity(request,id):
    cart_item = get_object_or_404(Cart,id=id,user=request.user)
    cart_item.food_item_quantity += 1
    cart_item.food_item_total = cart_item.food_item_quantity * cart_item.food_item.food_price
    cart_item.save()
    return redirect('cart')