from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData["first_name"]) < 3 or not str.isalpha(postData["first_name"]):
            errors["first_name"] = "Name must be at least 3 characters and contain no numbers"
        if len(postData["last_name"]) < 3 or not str.isalpha(postData["last_name"]):
            errors["last_name"] = "Name must be at least 3 characters and contain no numbers"
        if len(postData["username"]) < 3 or not str.isalpha(postData["username"]):
            errors["username"] = "Must enter a valid username address"
        if len(postData["password"]) < 8:
            errors["password"] = "Pasword must be at least 8 characters"
        if postData["confirm_pw"] != postData["password"] :
            errors["confirm_pw"] = "Passwords do not match"
        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    