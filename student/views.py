from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import student
from django.db.models import Avg
from student.models import Result, student, semester
    

def stu_index(request):
    student_list = student.objects.all()
    template = loader.get_template("student.html")
    context = {
        "latest_question_list": student_list,
    }
    return HttpResponse(template.render(context, request))


def student_sem(request,st_id) : 
    average_marks =Result.objects.filter(student_id=st_id).values('student_id', 'sem_id').annotate(average_marks=Avg('marks')).order_by('student_id', 'sem_id')
    template = loader.get_template("student_sem.html")
    context = {'average_marks': average_marks}
    return HttpResponse(template.render(context, request))
