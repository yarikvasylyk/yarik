from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()


class Comment(models.Model):
    pass


class Author(models.Model):
    pass

