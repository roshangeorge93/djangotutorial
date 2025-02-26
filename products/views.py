from django.shortcuts import render
from django.http import HttpResponse
from .models import Product ,Category
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.db.models import ExpressionWrapper , Sum ,Count,Avg, FloatField




def respond (request):
    return  HttpResponse("hello world")


# def resp (request ,element_id ):
#         try:
#             return HttpResponse( Employee.objects.get(id=element_id))
#         except ObjectDoesNotExist as E:
#             return  HttpResponse(f"employee with this {element_id} is not present {E}",404 )

             
#         print(Employee.objects.filter(id=element_id).values('ename'))
#         return HttpResponse( Employee.objects.filter(id=element_id).values('ename')[0]['ename'])

def resp (request ,element_id ):
    try:
        employee_obj = Product.objects.get(id=element_id)
        ans = Product.objects.filter(id=element_id).annotate(sgpa = ExpressionWrapper(Avg('result__marks'),output_field=FloatField())).values('result__sem','sgpa')

    except:
        return  HttpResponse(f"employee with this {element_id} is not present " )
    


    context ={
        'ans' : ans
    }
    
    return render(request, "one_student.html", context)
      

from django.http import HttpResponse


def index(request):
    leaf = Category.objects.get(cat_name= 'Mobiles')
    category_list = Category.objects.all()
    children_categories = []
    for category in category_list:
        if category.cat_id == leaf.pat_id:
            children_categories.append(category.cat_name)

    context = {
        "children_categories": children_categories ,
    }
    return render(request, "list_cat.html", context)

def index_leaf_root(request,cat_name):
    category_list = Category.objects.get(cat_name__iexact=pat_name)
   
    context = {
        "children_categories": children_categories ,
    }
    return render(request, "list_cat.html", context)
    




def resp (request ,element_id ):
    category_list = Category.objects.all()


