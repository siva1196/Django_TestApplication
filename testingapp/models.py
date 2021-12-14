from django.db import models
from django.db.models.base import Model

# Create your models here.

class Users(models.Model):
    Name = models.CharField(max_length=100)
    DOB = models.DateField()
    Gender = models.TextField() 
    City = models.TextField()
    Mobile = models.IntegerField()
    Email = models.TextField()
    Username = models.CharField(max_length=6)
