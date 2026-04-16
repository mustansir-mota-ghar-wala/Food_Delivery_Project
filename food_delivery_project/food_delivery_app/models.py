from django.db import models

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
