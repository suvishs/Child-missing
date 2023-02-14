from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.


class Police(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge_number = models.CharField(max_length=10, default='00000')

    def __str__(self):
        return self.user.username


class complainant(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    child_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    identification = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    img = models.ImageField(upload_to='gallary')
    staus = models.BooleanField(default=False)
    complintent = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name


class user(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    child_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    identification = models.TextField()
    Details = models.TextField()
    image = models.ImageField(upload_to='pics')
    staus = models.BooleanField(default=False)
    users = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name


class complainant_history(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    child_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    identification = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    staus = models.CharField(max_length=50)
    report = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class user_history(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    child_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    identification = models.TextField()
    Details = models.TextField()
    staus = models.CharField(max_length=50)
    report = models.CharField(max_length=255)

    def __str__(self):
        return self.name