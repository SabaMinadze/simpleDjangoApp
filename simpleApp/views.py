# simpleApp/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import BigBox
from .serializers import BigBoxSerializer

def index(request):
    products = BigBox.objects.all()
    return render(request, 'first.html', {"products": products})



def product(request):
    return render(request, 'product.html', {"name": "Hello world", "num1": 777})

class BigBoxViewSet(viewsets.ModelViewSet):
    serializer_class = BigBoxSerializer
    queryset = BigBox.objects.all()


