# mytcapp/models.py
from django.db import models
from django.contrib.auth.models import User

class TCRequest(models.Model):
    # Your other fields for TCRequest model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'mytcapp'

class TCRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    class Meta:
        app_label = 'mytcapp'
