from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)