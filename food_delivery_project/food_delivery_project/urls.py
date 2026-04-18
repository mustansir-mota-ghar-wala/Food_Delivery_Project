"""
URL configuration for food_delivery_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from food_delivery_app.views import Register,Login,Home,Logout,Food_items,cart,add_to_cart,remove_cart_item,decrease_quantity,increase_quantity
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',Register,name='register'),
    path('login',Login,name='login'),
    path('home',Home,name='home'),
    path('logout',Logout,name='logout'),
    path('food/item/<int:id>',Food_items,name='food_item'),
    path('cart/', cart, name='cart'),
    path('cart/add/<int:id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', remove_cart_item, name='remove_cart_item'),
    path('decrease/quantity/<int:id>',decrease_quantity,name='decrease_quantity'),
    path('increase/quantity/<int:id>',increase_quantity,name='increase_quantity'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
