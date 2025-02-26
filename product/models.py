from django.db import models

class Brand(models.Model) : 
    name = models.CharField()

class Category(models.Model) : 
    name = models.CharField()
    parent_cat_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class Product(models.Model):
    name = models.CharField()
    ratings = models.FloatField()
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)



