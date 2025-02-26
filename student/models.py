from django.db import models

# Create your models here.
class Semester(models.Model):
    pass

class Subject(models.Model):
    name = models.CharField(max_length=200)

class Student(models.Model):
    USN = models.CharField(unique=True)
    name = models.CharField()
    current_sem = models.PositiveIntegerField()


class Result(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.FloatField()

