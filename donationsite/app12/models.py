from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Registration(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    


class Donate(models.Model):
    name=models.CharField(max_length=100)
    amount = models.CharField(max_length=100 , blank=True)
    email=models.CharField(max_length=100)
   