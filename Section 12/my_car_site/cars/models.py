from django.db import models

# Create your models here.
class Car(models.Model):
  # pk 
  brand = models.CharField(max_length=30)
  year = models.IntegerField()

  def __str__(self):
    return f'PK: {self.pk} >> Car is {self.brand}, model: {self.year}'

# after that --> python manage.py makemigrations cars