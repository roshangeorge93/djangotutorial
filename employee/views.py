from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Employee
from django.template import loader

# Create your views here.

def employees(request,employee_id):
    details = Employee.objects.filter(id=employee_id).values()
    lis = [details[0]['id'], details[0]['name'] , details[0]['email'] ,details[0]['designation']]
    answer =''
    for i in lis:
        answer+=" -> "+str(i)
    # print(name)
    # if Employee.objects.filter(id=employee_id).values('name'):
    return HttpResponse(answer)
    # else:
    #     raise Exception("No employee")


def index(request):
    latest_employee_list = Employee.objects.all()
    template = loader.get_template("index.html")
    context = {
        "latest_employee_list": latest_employee_list,
    }
    return HttpResponse(template.render(context, request))

# def employeedetails(request, employee_id):
#     name = Employee.objects.filter(id=employee_id).values('name')
#     return HttpResponse(name)