from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader



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
        employee_obj = Employee.objects.get(id=element_id)
    except:
        return  HttpResponse(f"employee with this {element_id} is not present " )
    
    employee ={
        'name' : employee_obj.ename,
        'id': employee_obj.eid,
        'Designation': employee_obj.designation
    }

    context ={
        'employee' : employee
    }
    
    return render(request, "emp_details.html", context)
      

from django.http import HttpResponse


def index(request):
    employee_list = Employee.objects.all()
    template = loader.get_template("index.html")
    context = {
        "employee_list": employee_list ,
    }
    return render(request, "index.html", context)
    



# Leave the rest of the views (detail, results, vote) unchanged


# def resp (request ,element_id ):
#     if Employee.objects.filter(id=element_id).exists():
#         print(Employee.objects.filter(id=element_id).values('ename'))
#         return HttpResponse( Employee.objects.get(id=element_id))
#         return HttpResponse( Employee.objects.filter(id=element_id).values('ename')[0]['ename'])


#     return  HttpResponse(f"employee with this {element_id} is not present")

# Create your views here.
