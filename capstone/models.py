from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"
    

class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, default=None)
    time_and_date = models.DateTimeField(default=None)
    users = models.ManyToManyField(User)
    def __str__(self):
        return f"The group {self.name} with the activity {self.activity} and the Group Members: {self.users}."
    
