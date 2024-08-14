from django.db import models

# Create your models here.
class stock(models.Model):
    sno =models.IntegerField()
    arriveddate =models.DateField()
    productName= models.CharField(max_length=20 )
    productQ =models.CharField(max_length=5)
    productP= models.FloatField()
