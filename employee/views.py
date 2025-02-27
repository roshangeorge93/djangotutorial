from django.shortcuts import render
from django.http import HttpResponse,Http404
from employee.models import Employee

def detail(request,em_id) : 
    employees = Employee.objects.filter(id=em_id).values('id')
    if employees: 
        employe = Employee.objects.filter(id=em_id)
        # import ipdb;ipdb.set_trace()
        response = "id : %s"%employe[0].id, " Employee name : %s"%employe[0].name,  " salary : %s"%employe[0].salary, " Designation : %s "%employe[0].designation
        return HttpResponse(response)
    else: 
        return Http404('no found')
    

from django.http import HttpResponse
from django.template import loader
from .models import Employee


def index(request):
    employee_list = Employee.objects.all()
    template = loader.get_template("index.html")
    context = {
        "latest_question_list": employee_list,
    }
    return HttpResponse(template.render(context, request))


