from django.db import models

# Create your models here.
class Teacher(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  subject = models.CharField(max_length=30)
  qualification = models.CharField(default='MSC',max_length=50)
  deparment = models.CharField(default= 'Engineering', max_length=50)
  specialization = models.CharField(default='Engineering',max_length=50)
  number_of_subjects = models.IntegerField(default=1)

  def __str__(self):
    return f'{self.first_name} {self.last_name} teaches {self.subject}'