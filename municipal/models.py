from django.db import models

class Municipal(models.Model):
    municipal_name = models.CharField(max_length=150)
    person_in_charge = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'municipal'
# Create your models here.
