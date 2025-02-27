from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from Employee.models import Employee


    
def index(request):
    employee_list = Employee.objects.all()
    template = loader.get_template("index.html")
    context = {
        "employee_list": employee_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, employee_id):   
    if Employee.objects.filter(id=employee_id).exists(): 
        # emp_name=Employee.objects.filter(id=employee_id).values('name')[0]['name']
        emp=Employee.objects.get(id=employee_id)
        response='Employee details:%s' % emp.name,', salary:%s' %emp.salary,' , designation:%s'%emp.designation
        return HttpResponse(response)
    else:
        return HttpResponse('Does not exists')
    
def test(request):
    template = loader.get_template("test.html")
    return HttpResponse(template.render(request))


