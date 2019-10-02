from django.db import models
from datetime import datetime 

# Create your models here.

class Product(models.Model):
    
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    sold  = models.IntegerField()
    stock = models.IntegerField()  

class Alerts(models.Model):

    alert = models.TextField(max_length=250)
    date = models.DateTimeField(default=datetime.now, blank=True)
    offer = models.BooleanField(default=True)