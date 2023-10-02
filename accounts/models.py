from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.decorators import classonlymethod

# Create your models here.
class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    image = models.ImageField(upload_to="admins")
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name= models.CharField(max_length=200)
    address= models.CharField(max_length=200,null=True,blank=True)
    mobile=models.CharField(max_length=10)
    joined_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.joined_on.strftime('%Y-%m-%d %H:%M:%S')})"