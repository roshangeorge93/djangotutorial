from django.db import models



class Location(models.Model):
    l_id= models.AutoField(primary_key = True)
    l_name=models.CharField(max_length=200)
    l_city=models.CharField(max_length=200)
    l_state=models.CharField(max_length=200)
    l_country=models.CharField(max_length=200)


class Department(models.Model):
    department_id=models.AutoField(primary_key = True)
    department_name=models.CharField(max_length=200)
    l=models.ForeignKey(
        "Location", on_delete=models.CASCADE)

class Employee(models.Model):
    
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Designation= models.CharField(max_length=200)
    Salary=models.FloatField(max_length=200)
    department=models.ForeignKey(
        "Department", on_delete=models.CASCADE)
    Experience=models.SmallIntegerField()

class Contact(models.Model):
    Number=models.CharField(max_length=200)
    Adress=models.CharField(max_length=200)
    Emp= models.ForeignKey(
        "Employee", on_delete=models.CASCADE)


# Create your models here.
