from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    isBlocked = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)