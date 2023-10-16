

from django.db import models


class RegisterModel(models.Model):
    
    
    username = models.CharField(max_length=100, default='abcd')
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email_id = models.EmailField()
    mobile_num = models.TextField(default='+880')
    study_level = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    age = models.ImageField()
    address = models.TextField(default='Address')
    password1 = models.TextField(max_length=100,default='123')
    password2 = models.TextField(max_length=100, default='123')
    # mail_address = models.EmailField()
    # mobile = models.TextField(default='+880')
      
    def __str__(self):
        return self.name
    

















# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=150, blank=True, null=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

