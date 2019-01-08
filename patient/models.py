from django.db import models

class Patient(models.Model):
    username = models.SlugField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    number = models.CharField(max_length=20)
    email_address = models.CharField(max_length=100)
    
    

class Meta:
    db_table = 'patient'
# Create your models here.
