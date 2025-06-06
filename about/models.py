from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


    def __str__(self):
        return f"Collaboration request from {self.name}"