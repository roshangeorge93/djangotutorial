from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from employee.models import Employee
from django.template import loader
from .models import Category, Product


# Create your views here.

def parents(request):
    leaf = Category.objects.get(name='cat_name2')
    cat_list = Category.objects.all()
    child_categories=[]
    for cat in cat_list:
        if cat.id == leaf.parent_category_id_id:
            child_categories.append(cat.name)
            pass
    context = {
        'child_categories': child_categories,
    }
    return render(request, 'category.html', context)


def product_list(request):
    latest_product_list = Product.objects.all()
    template = loader.get_template("product.html")
    context = {
        "latest_product_list": latest_product_list,
    }
    return HttpResponse(template.render(context, request))

def product_details(request,product_id):
    details = Product.objects.filter(id=product_id).values()
    # lis = [details[0]['id'], details[0]['name'] , details[0]['ratings'] ,details[0]['price'], details[0]['brand_id'], details[0]['category_id']]
    # answer =''
    # for i in lis:
    #     answer+=" -> "+str(i)
    
    return HttpResponse(details)