from django.db import models

class semester(models.Model): 
    pass 
class subject(models.Model) : 
    name = models.CharField()

class student(models.Model) : 
    name = models.CharField()
    usn = models.CharField(unique=True)
    current_sem = models.PositiveSmallIntegerField()

class Result(models.Model) : 
    marks = models.FloatField()
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    sem = models.ForeignKey(semester,on_delete=models.CASCADE)
    sub = models.ForeignKey(subject,on_delete=models.CASCADE)
