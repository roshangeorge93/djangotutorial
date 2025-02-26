from django.shortcuts import render
from django.http import HttpResponse
from .models import Product ,Category
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.db.models import ExpressionWrapper , Sum ,Count,Avg, FloatField


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
    # I couldn't directly do a self join and I will Mobiles dynamically
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

    


def resp (request ,element_id ):
    category_list = Category.objects.all()


