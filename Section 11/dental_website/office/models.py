from django.db import models

# Create your models here.
class Patient(models.Model):

  # Check model field reference in the django documentation
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  age = models.IntegerField()