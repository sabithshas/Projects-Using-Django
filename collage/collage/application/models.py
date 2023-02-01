from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Add_hod(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    Department=models.CharField(max_length=15)
    qualification=models.CharField(max_length=15)
    experience=models.CharField(max_length=100)
    password=models.CharField(max_length=15)
    confirmpassword=models.CharField(max_length=15)
    role=models.CharField(max_length=10)
    status=models.CharField(max_length=30)
    def __str__(self):
        return self.Firstname

class Add_teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Hfirstname=models.CharField(max_length=30)
    Hlastname=models.CharField(max_length=30)
    Husername=models.CharField(max_length=20)
    Hadress=models.CharField(max_length=50)
    Hplace=models.CharField(max_length=30)
    Hphone=models.IntegerField()
    Hemail=models.EmailField()
    Hdepartment=models.CharField(max_length=15)
    Hsubject=models.CharField(max_length=15)
    Hqualification=models.CharField(max_length=30)
    Hexperience=models.CharField(max_length=50)
    Hpassword=models.CharField(max_length=15)
    Hcpassword=models.CharField(max_length=15)
    role=models.CharField(max_length=10)
    status=models.CharField(max_length=30)
    def __str__(self):
        return self.Hfirstname

class Add_students(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Sfirstname=models.CharField(max_length=30)
    Slastname=models.CharField(max_length=30)
    Susername=models.CharField(max_length=20)
    Sadress=models.CharField(max_length=50)
    Splace=models.CharField(max_length=30)
    Sphone=models.IntegerField()
    Semail=models.EmailField()
    Sdepartment=models.CharField(max_length=15)
    Ssubject=models.CharField(max_length=15)
    SAdmission=models.IntegerField()
    Spassword=models.CharField(max_length=15)
    Scpassword=models.CharField(max_length=15)
    Srole=models.CharField(max_length=10)
    Sstatus=models.CharField(max_length=30)
    def __str__(self):
        return self.Sfirstname
   
class leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(max_length=10)
    reason=models.CharField(max_length=70)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=10)
    def __str__(self):
        return self.reason

class notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(max_length=10)
    notification=models.CharField(max_length=100)
    role=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    department=models.CharField(max_length=40)
    def __str__(self):
        return self.notification

class mark(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=40)
    subject=models.CharField(max_length=40)
    total=models.CharField(max_length=40)
    mymark=models.CharField(max_length=40)
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.subject

