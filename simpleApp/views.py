from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import BigBox, Offer
from .serializers import BigBoxSerializer

def index(request):
    products = BigBox.objects.all()
    return render(request, 'first.html', {"products": products})


def about(request):
    offer = Offer.objects.all()
    return render(request, 'about.html', {"offer":offer})


def product(request):
    return render(request, 'product.html', {"name": "Hello world", "num1": 777})


class BigBoxViewSet(viewsets.ModelViewSet):
    queryset = BigBox.objects.all()
    serializer_class = BigBoxSerializer