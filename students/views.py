from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from students.models import Student,Result
from django.db.models import Sum,Count
from django.db.models import ExpressionWrapper, FloatField

def index(request):
    student_list=Student.objects.all()
    template = loader.get_template("student.html")
    context = {
        "student_list": student_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, student_id):   
    if Student.objects.filter(id=student_id).exists(): 
        result_list=Student.objects.filter(id=student_id).annotate(t_percentage=ExpressionWrapper((Sum('result__marks') / Count('result__subject')),output_field=FloatField())).values('result__semester','t_percentage')
        template = loader.get_template("results.html")
        context = {
        "result_list": result_list,
        }

        return HttpResponse(template.render(context, request))

    else:
        return HttpResponse('Does not exists')



