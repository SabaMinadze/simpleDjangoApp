from django.shortcuts import render
from .models import BigBox, Offer

def index(request):
    products = BigBox.objects.all()
    return render(request, 'first.html', {"products": products})


def about(request):
    offer = Offer.objects.all()
    return render(request, 'about.html', {"offer":offer})


def product(request):
    return render(request, 'product.html', {"name": "Hello world", "num1": 777})

