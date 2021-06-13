from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # postData == request.POST
        if len(postData['title']) < 2:
            errors["title"] = "Title is too short, must be at least 2 characters long!"
        if len(postData['network']) <3:
            errors["network"] = "Network is too short, must be at least 3 characters long!"
        if len(postData['description']) > 0:
            if len(postData['description']) < 10:
                errors["description"] = "Description is too short, must be at least 10 characters long!"
        return errors



# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


