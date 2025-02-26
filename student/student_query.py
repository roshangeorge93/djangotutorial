from student.models import Student,Semester,Marks,Subject
from django.db.models import Avg,Sum,FloatField,Count,ExpressionWrapper

#  Get all distinct sem of student

q0 = Student.objects.values_list('Current_sem',flat=True ).distinct().all()
for q in q0:
    print(q)