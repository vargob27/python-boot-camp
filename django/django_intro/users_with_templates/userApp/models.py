from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.TextField(max_length=255)
    lastName = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)