from django.db import models

# Create your models here.

class Semester(models.Model):
    Sem_id=models.SmallIntegerField(primary_key = True)
    Sem=models.SmallIntegerField()
   
    

class Student(models.Model):
    Usn=models.CharField(max_length=100)
    Name=models.CharField(max_length=200)
    Branch=models.CharField(max_length=100)
    Current_sem=models.SmallIntegerField()


class Subject(models.Model):
    Sub_Id=models.BigAutoField(primary_key = True)
    Sub_name=models.CharField()
   

class Marks(models.Model):
    Student_Id=models.ForeignKey(
        "Student", on_delete=models.CASCADE)
    Sub_Id=models.ForeignKey(
        "Subject", on_delete=models.CASCADE)
    Marks=models.FloatField(max_length=100)
    Sem_Id=models.ForeignKey(
        "Semester", on_delete=models.CASCADE)
    

  