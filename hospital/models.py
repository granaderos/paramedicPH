from django.db import models

class Hospital(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    hospitalName = models.CharField(max_length=200)
    personInCharge = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    telephone = models.CharField(max_length=20)
   
    class Meta: 
        db_table = 'hospital'
# Create your models here.
