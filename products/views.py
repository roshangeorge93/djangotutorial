from django.shortcuts import render

# Create your views here.


# Create your views here.
from django.http import HttpResponse


def products(request):
    return HttpResponse("Hello, world. You're at the product index.")