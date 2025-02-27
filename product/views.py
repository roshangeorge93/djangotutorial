from django.shortcuts import render
from product.models import Product, Category, Brand
from django.http import HttpResponse, Http404
from django.template import loader


def product_detail(request,pr_id) : 
    products = Product.objects.filter(id=pr_id).values('id')
    if products: 
        prod = Product.objects.filter(id=pr_id)
        # import ipdb;ipdb.set_trace()
        response = "id : %s"%prod[0].id, "Product_name : %s"%prod[0].name,  " salary : %s"%prod[0].ratings, " Designation : %s "%prod[0].price, " Designation : %s "%prod[0].brand_id, " Designation : %s "%prod[0].category_id
        return HttpResponse(response)
    else: 
        return Http404('no found')
    

def product_index(request):
    product_list = Product.objects.all()
    template = loader.get_template("product.html")
    context = {
        "latest_question_list": product_list,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    leaf = Category.objects.get(name='cname6')
    cat_list = Category.objects.all()
    sub_categories=[]
    for cat in cat_list:
        if cat.id == leaf.parent_cat_id_id:
            sub_categories.append(cat.name)
            pass
    context = {
        'sub_categories': sub_categories,
    }
    return HttpResponse (sub_categories)
