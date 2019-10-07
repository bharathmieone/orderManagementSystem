from django.db import models
from datetime import datetime

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=100)
    price = models.IntegerField()
    sold = models.IntegerField()
    stock = models.IntegerField()
    tasks = models.IntegerField()
    pending = models.IntegerField()
    

    def __str__(self):
        return self.title


class Alerts(models.Model):

    alert = models.TextField(max_length=250)
    date = models.DateTimeField(default=datetime.now, blank=True)
    offer = models.BooleanField(default=True)

    def __str__(self):
        return self.alert


class Earnings(models.Model):
    # Displaying data
    jan = models.IntegerField()
    feb = models.IntegerField()
    mar = models.IntegerField()
    apr = models.IntegerField()
    may = models.IntegerField()
    jun = models.IntegerField()
    jul = models.IntegerField()
    aug = models.IntegerField()
    sep = models.IntegerField()
    octo = models.IntegerField()
    nov = models.IntegerField()
    dec = models.IntegerField()

    # Display title
    jant = models.TextField()
    febt = models.TextField()
    mart = models.TextField()
    aprt = models.TextField()
    mayt = models.TextField()
    junt = models.TextField()
    jult = models.TextField()
    augt = models.TextField()
    sept = models.TextField()
    octot = models.TextField()
    novt = models.TextField()
    dect = models.TextField()

    def __str__(self):
        return 'Monthly Earnings'
