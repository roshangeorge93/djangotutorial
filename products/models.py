from django.db import models

# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=200)

class Category(models.Model):
    name=models.CharField(max_length=200)
    parent_category=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    rating=models.SmallIntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

