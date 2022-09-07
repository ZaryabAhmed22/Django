import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Genre, Language, Book, BookInstance
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
  num_books = Book.objects.all().count()
  num_instacnes = BookInstance.objects.all().count()

  num_instacnes_avail = BookInstance.objects.filter(status__exact='a').count()

  context = {
    'num_book': num_books,
    'num_instances': num_instacnes,
    'num_instances_avail': num_instacnes_avail
  }

  return render(request, 'catalog/index.html', context=context)

class BookCreate(CreateView): #book_form.html
  model = Book
  fields = '__all__'

  #success_url = reverse_lazy('catalog:index')

class BookDetail(DetailView): #book_detail
  model = Book

@login_required
def my_view(request):
  return render(request, 'catalog/my_view.html')
