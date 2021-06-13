from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['course_name']) < 6:
            errors['name'] = "Course name is too short! Must be at least 6 characters!"
        if len(reqPOST['description']) < 16:
            errors['desc'] = "Description is too short! Must be at least 16 characters!"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()