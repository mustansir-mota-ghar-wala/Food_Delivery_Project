from django.contrib import admin
from .models import Restaurant,Food_Items,Order,OrderItem
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food_Items)
admin.site.register(Order)
admin.site.register(OrderItem)