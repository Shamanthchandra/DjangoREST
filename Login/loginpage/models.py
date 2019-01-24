from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    fullname = models.CharField(max_length=60)
    email_id = models.EmailField()
    dob = models.DateField()
