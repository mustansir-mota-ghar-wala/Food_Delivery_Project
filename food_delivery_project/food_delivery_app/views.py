from django.shortcuts import render
from .models import Restaurant
# Create your views here.

def Home(request):
    restaurant = Restaurant.objects.all()
    context = {'restaurents':restaurant}
    return render(request,'home.html',context)