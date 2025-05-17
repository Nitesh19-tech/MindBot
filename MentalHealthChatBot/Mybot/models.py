from django.db import models

# Create your models here.

class Registration(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    emailaddress=models.CharField(max_length=50,primary_key=True)
    regdate=models.CharField(max_length=30)

class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=30)