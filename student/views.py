from django.shortcuts import render
from student.models import Student, Result
from django.http import HttpResponse
from django.template import loader
from django.db.models import ExpressionWrapper, Avg, Sum, FloatField, Count

# Create your views here.

def student_list(request):
    latest_employee_list = Student.objects.all()
    template = loader.get_template("student.html")
    context = {
        "latest_employee_list": latest_employee_list,
    }
    return HttpResponse(template.render(context, request))


def student(request,student_id):
    if Student.objects.filter(id=student_id).exists():
        results = Student.objects.filter(id=student_id).annotate(SGPA = ExpressionWrapper((Sum('result__marks')/Count('result__subject')), output_field=FloatField())).values('result__semester', 'SGPA').order_by('result__semester')
        template = loader.get_template('result.html')
        
        context = {
            "student_result_list": results,
        }
        return HttpResponse(template.render(context, request))
    
    else:
        return HttpResponse("No student results found") 
