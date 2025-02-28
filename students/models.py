from django.db import models

class Student(models.Model):
    usn = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=20)
    std = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
         return self.name

class Result(models.Model):
    sem = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"Result for {self.student.name} in {self.subject.name}, Sem {self.sem}: {self.marks}"
