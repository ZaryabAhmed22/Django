from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length=150)

  def __str__(self):
    return f'{self.name}'

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey('Author', on_delete=models.SET_NULL) 
  # model.SET_NULL --> null value if no author is selected or the author is deleted
  # ForeignKey('Author') --> this model is linked to the Author model
  # MORE TO COME HERE FOR BOOK

class Author(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  date_of_birth = models.DateField(null=True, blank=True)
  date_of_death = models.DateField(null=True, blank=True)

  class Meta:
    ordering = ['last_name', 'first_name']

  def get_absolute_url(self):
      return reverse("author_detail", kwargs={"pk": self.pk})
  
  def __str__(self):
    return f'{self.last_name}, {self.first_name}'