from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from student.models import Student,Semester,Marks,Subject
from django.db.models import Avg,Sum,FloatField,Count,ExpressionWrapper

# def student(request):
#     return HttpResponse("Hello, world. You're at the student index.")

def display(request,student_id):
    Marks_list=Student.objects.filter(id=student_id).annotate(sem_percentage=ExpressionWrapper((Sum('marks__Marks') / Count('marks__Sub_Id')),output_field=FloatField())).values('marks__Sem_Id','sem_percentage')
    context = {
        "Marks_list": Marks_list,
    }
    
    
    return render(request, "marks.html", context)
  

def index(request):
    student_list = Student.objects.all()
    
    context = {
        "student_list": student_list,
    }
    
    return render(request, "student.html", context)
