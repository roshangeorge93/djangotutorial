from student.models import Student,Semester,Marks,Subject
from django.db.models import Avg,Sum,FloatField,Count,ExpressionWrapper

#  Get all distinct sem of student

q0 = Student.objects.values_list('Current_sem',flat=True ).distinct().all()
for q in q0:
    print(q)


# list all student belonging to sem 1
q1=Student.objects.filter(Current_sem='1').values_list('Name',flat=True)
for q in q1:
    print(q)


# -- get all marks of a student given usn for the latest seem
cur_sem=Student.objects.filter(Usn='vv006').values_list('Current_sem',flat=True).first()
q3=Marks.objects.filter(Student_Id__Usn='vv006').filter(Sem_Id__Sem=cur_sem).values_list('Marks',flat=True)
for q in q3:
    print(q)


# -- get all marks of a student given usn for a particular subject
sub=Subject.objects.filter(Sub_name='DS').values_list('Sub_Id',flat=True).first()
q4=Marks.objects.filter(Student_Id__Usn='vv003').get(Sub_Id=sub)
print(q4.Marks)


# -- get the total percentage of marks for a student in particular sem

q5=Marks.objects.filter(Student_Id__Usn="vv001", Sem_Id__Sem=1).aggregate(Avg("Marks", default=0))
print(q5)