from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurant(models.Model):
    CATEGORY_CHOICES = [
        ('Veg','Veg'),
        ('Non-Veg', 'Non-Veg'),
        ('Both', 'Veg & Non-Veg'),
        
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='restaurants')

    def __str__(self):
        return self.name

class Food_Items(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='restaurant')
    food_name = models.CharField()
    food_description = models.TextField()
    food_image = models.ImageField(upload_to='food_image')
    food_price = models.IntegerField()
    def __str__(self):
        return self.food_name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    food_item = models.ForeignKey(Food_Items,on_delete=models.CASCADE)
    food_item_quantity = models.IntegerField(default=1)
    food_item_total = models.IntegerField()