from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# Create your models here.
class Doctorregistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    specialised=models.CharField(max_length=120)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=50)
    def __str__(self):
        return self.fullname

class Patientregistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=50)
    def __str__(self):
        return self.fullname

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.department

class Medicine(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    date=models.DateField()
    diagnosis=models.CharField(max_length=500)
    drugname=models.CharField(max_length=500)
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    reason=models.CharField(max_length=100)  
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.reason
        