from django.contrib import admin
from .models import Product, Alerts, Earnings

# Register your models here.

admin.site.register(Product)
admin.site.register(Alerts)
admin.site.register(Earnings)
