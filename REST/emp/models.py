from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(unique=True, null=False, primary_key=True)
    firstname = models.CharField(max_length=10, null=False)
    lastname= models.CharField(max_length=10)
    designation = models.CharField(max_length=25)
    department = models.CharField(max_length=10)
    age = models.IntegerField(null=False, default=25)

    def __str__(self):
        return self.firstname + " " + self.lastname