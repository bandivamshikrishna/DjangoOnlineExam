from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField(blank=True)
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=100)
    