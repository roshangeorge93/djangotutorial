from django.db import models

# Create your models here.
class Sem(models.Model):
    semester_number=models.SmallIntegerField()

class Student(models.Model):
    usn=models.CharField(max_length=200)
    name=models.CharField(max_length=200,unique=True)
    current_sem=models.SmallIntegerField()

class Subject(models.Model):
    name=models.CharField(max_length=200)

class Result(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE) 
    subject= models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.DecimalField(max_digits=10,decimal_places=2)
    semester=models.ForeignKey(Sem,on_delete=models.CASCADE)


