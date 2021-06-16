from django.db import models
# from django.db.models.base import Model
# from django.db.models.fields import EmailField
import re
import bcrypt


# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}
        existing_users = User.objects.filter(email=post_data['email'])
        #length of the first name
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be 2 characters or more"
        # length of last NameError
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be 2 characters or more"
        # email matches format
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')
        if len(post_data['email'])==0:
            errors['email'] = "You must enter an email"
        elif not email_regex.match(post_data['email']):
            errors['email'] = "Must be a valid email"
        # email is unique
        current_users = User.objects.filter(email = post_data['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "Email already in use"
        # password was entered
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        #matches
        if post_data['password'] != post_data['confirm_password']:
            errors['nonmatch'] = "Your password does not match"
        return errors
    
    def login_validator(self, post_data):
        errors = {}
        existing_user = User.objects.filter(email=post_data['email'])
        if len(post_data['email']) == 0:
            errors['email'] = "Enter email"
        if len(post_data['password']) < 8:
            errors['password'] = "Enter 8 character password"
        elif bcrypt.checkpw(post_data['password'].encode(), existing_user[0].password.encode()) != True:
            errors['nonmatch'] = "Email and password do not match"

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
