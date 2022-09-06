from django.db import models

# Create your models here.
class Teacher(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  subject = models.CharField(max_length=30)
  qualification = models.CharField(default='MSC',max_length=50)
  deparment = models.CharField(default= 'Department Of', max_length=50)
  specialization = models.CharField(default='Engineering',max_length=50)
  number_of_subjects = models.IntegerField(default=1)
  gender = models.CharField(default='Male',max_length=5)


  def __str__(self):
    string = f'{self.first_name} {self.last_name} teaches {self.subject}, is {self.qualification} in {self.specialization}. He is assossiated to the {self.deparment} and teaching a total of {self.number_of_subjects} subjects.'
    return string