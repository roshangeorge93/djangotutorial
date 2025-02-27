from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from products.models import Product,Category


    
def index(request):
    product_list = Product.objects.all()
    template = loader.get_template("products.html")
    context = {
        "product_list": product_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, product_id):   
    if Product.objects.filter(id=product_id).exists(): 
        product=Product.objects.get(id=product_id)
        response='Product details:%s' % product.name,', price:%s' %product.price,' , rating:%s' %product.rating, ', brand:%s '%product.brand.name
        return HttpResponse(response)
    else:
        return HttpResponse('Does not exists')



    
def category(request,category_id):
    parent_cat= Category.objects.get(id=category_id)
    category_list=Category.objects.all()
    sub_categories=[]
    for category in category_list:
        if category.parent_category_id==parent_cat.id:
             sub_categories.append(category.name)
      
    template = loader.get_template("category.html")
    context = {
        "sub_categories": sub_categories,
    }
    return HttpResponse(template.render(context, request))

    
def main(request):
    category_list =Category.objects.all()
    template = loader.get_template("main_category.html")
    context = {
        "category_list": category_list,
    }
    return HttpResponse(template.render(context, request))
