from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    description = models.TextField(default="")

    def __str__(self):
        return '{}'.format(self.name)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, related_name='ninjas')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)