from django.db import models

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