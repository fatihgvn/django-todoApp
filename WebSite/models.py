from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=35)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class todolist(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    iDo = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
