from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Class=models.IntegerField()
    Roll=models.IntegerField()
    Dept=models.CharField(max_length=100)