from django.shortcuts import render
from .models import Employee

# Create your views here.
from django.http import HttpResponse


def employee(request,employee_id):
    Employee_details=Employee.objects.filter(id=employee_id).values()
    
    
    context = {
        "Employee_details": Employee_details,
    }
    
    return render(request, "Employee_details.html", context)
  
# def detail(request, employee_id):

#     return HttpResponse("You're looking at employee %s." % employee_id)


# def results(request, employee_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % employee_id)


# def vote(request, employee_id):
#     return HttpResponse("You're voting on question %s." % employee_id)



from django.template import loader




def index(request):
    employee_list = Employee.objects.all()
    
    context = {
        "employee_list": employee_list,
    }
    
    return render(request, "index.html", context)
