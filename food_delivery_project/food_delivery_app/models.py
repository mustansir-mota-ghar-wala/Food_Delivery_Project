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
    image = models.ImageField(upload_to='restaurants/')

    def __str__(self):
        return self.name