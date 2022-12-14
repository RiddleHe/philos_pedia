from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):

    title = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    owner = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title


class Entry(models.Model):
    topic = models.ForeignKey(Topic, default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)


    def __str__(self):
        return self.title

