from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.db.models import ExpressionWrapper , Sum ,Count,Avg, FloatField




def resp (request ,element_id ):
    try:
        #aggregate Query
        employee_obj = Student.objects.get(id=element_id)
        ans = Student.objects.filter(id=element_id).annotate(sgpa = ExpressionWrapper(Avg('result__marks'),output_field=FloatField())).values('result__sem','sgpa')

    except:
        return  HttpResponse(f"employee with this {element_id} is not present " )
   

    context ={
        'ans' : ans
    } 
    return render(request, "one_student.html", context)
      
from django.http import HttpResponse


def index(request):
    employee_list = Student.objects.all()
    context = {
        "employee_list": employee_list ,
    }
    return render(request, "all_students.html", context)
    



# Leave the rest of the views (detail, results, vote) unchanged


# def resp (request ,element_id ):
#     if Employee.objects.filter(id=element_id).exists():
#         print(Employee.objects.filter(id=element_id).values('ename'))
#         return HttpResponse( Employee.objects.get(id=element_id))
#         return HttpResponse( Employee.objects.filter(id=element_id).values('ename')[0]['ename'])


#     return  HttpResponse(f"employee with this {element_id} is not present")

# Create your views here.
