from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Employee
from django.template import loader
from .models import Category, Product


# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})
