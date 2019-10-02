from django.shortcuts import render, redirect
from .models import Product, Alerts
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):

    prod = Product.objects.all()
    alerts = Alerts.objects.all()
    current_user = request.user

    return render(request, "index.html", {"prod": prod, "alerts": alerts, "user": current_user.first_name})
