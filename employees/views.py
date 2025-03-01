from django.shortcuts import render
from .models import Employee

# Create your views here.
from django.http import HttpResponse


def employee(request,employee_id):
    Employee_details=Employee.objects.filter(id=employee_id).select_related('department__l').all()
    
    
    
    context = {
        "Employee_details": Employee_details,
    }
    
    return render(request, "Employee_details.html", context)
  




from django.template import loader




def index(request):
    employee_list = Employee.objects.select_related('department__l').all()
    
    context = {
        "employee_list": employee_list,
    }
    
    return render(request, "index.html", context)


def test(request):
    
    return render(request,"test.html")