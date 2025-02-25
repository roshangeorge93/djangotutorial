from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def product(request):
    return HttpResponse("Hello, world. You're at the product index.")