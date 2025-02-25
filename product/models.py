from django.db import models


# Create your models here.

class Brand(models.Model):
    B_Id=models.BigIntegerField(primary_key = True)
    B_name=models.CharField(max_length=100)
   
    

class Catageory(models.Model):
    Cat_Id=models.BigIntegerField(primary_key = True)
    Cat_name=models.CharField(max_length=200)
    Parent_Id=models.ForeignKey(
        "Catageory", on_delete=models.CASCADE)
   


class Product(models.Model):
    P_Id=models.BigIntegerField(primary_key = True)
    P_name=models.CharField()
    Cat_Id=models.ForeignKey(
        "Catageory", on_delete=models.CASCADE)
   
    B_Id=models.ForeignKey(
        "Brand", on_delete=models.CASCADE)
   




    

  






