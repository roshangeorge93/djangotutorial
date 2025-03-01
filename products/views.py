from django.shortcuts import render
from products.models import Product,Brand,Catageory
from django.db.models import F
# Create your views here.


# Create your views here.
from django.http import HttpResponse




# def products(request,employee_id):
#     Employee_details=Product.objects.filter(id=employee_id).values()
    
    
#     context = {
#         "Employee_details": Employee_details,
#     }
    
#     return render(request, "Employee_details.html", context)

def display(request,product_P_Id):
    product_details=Product.objects.filter(P_Id=product_P_Id).values()
    
    
    context = {
        "product_details": product_details,
    }
    
    return render(request, "product_details.html", context)

def index(request):
    product_list = Product.objects.all()
    
    context = {
        "product_list": product_list,
    }
    
    return render(request, "products.html", context)

def catageory(request):
    category_list = Catageory.objects.all()
    
    context = {
        "category_list": category_list,
    }
    
    return render(request, "catageory.html", context)

def sub_categeories(request,catageory_Cat_Id):
    sub_categeories=Catageory.objects.filter(Parent__isnull=False,Parent=catageory_Cat_Id).values(
    parent_cat=F('Parent__Cat_name'), 
    sub_cat=F('Cat_name')
)
    
    context = {
        "sub_categeories": sub_categeories,
    }
    
    return render(request, "sub_categeories.html", context)