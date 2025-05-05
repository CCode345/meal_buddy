from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=200, default='https://www.google.com/url?sa=i'
    '&url=https%3A%2F%2Fwww.theodysseyrestaurant.com%2F&psi' \
    'g=AOvVaw2gyu0awhbj5ADPjOBtjQAd&ust=1746486931934000&source=ima' \
    'ges&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODI-v74io0DFQAAAAAdAAAAABAE')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()

class Item(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name = "items")

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    is_veg = models.BooleanField(default=True)
    picture = models.URLField(max_length=200, default='https://www.google.com/url?sa=i'
    '&url=https%3A%2F%2Fwww.theodysseyrestaurant.com%2F&psi' \
    'g=AOvVaw2gyu0awhbj5ADPjOBtjQAd&ust=1746486931934000&source=ima' \
    'ges&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODI-v74io0DFQAAAAAdAAAAABAE')
    
