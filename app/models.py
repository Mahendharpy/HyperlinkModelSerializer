from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField(unique=True)
class Patient(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(unique=True)
