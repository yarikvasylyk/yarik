from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class Topic(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()





