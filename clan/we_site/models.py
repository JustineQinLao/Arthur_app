from django.contrib.auth.models import User
from django.db import models

class UserTheme(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_dark_theme = models.BooleanField(default=False)



class Members(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, blank=True)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    is_superuser = models.BooleanField(default=False)