from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    living_group = models.CharField(max_length=200)
    date_joined = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
    	return str(self.id) + " - " + self.first_name + " " + self.last_name

class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name