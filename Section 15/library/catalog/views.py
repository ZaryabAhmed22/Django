import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Genre, Language, Book, BookInstance
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


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

# VIEW LEVEL AUTH
# --> for Class Based Views we use Mixins
class BookCreate(LoginRequiredMixin, CreateView): #book_form.html
  model = Book
  fields = '__all__'

  #success_url = reverse_lazy('catalog:index')

class BookDetail(DetailView): #book_detail
  model = Book


# VIEW LEVEL AUTH
# --> for functional views we use Decorators 
@login_required
def my_view(request):
  return render(request, 'catalog/my_view.html')

# Creating a model form for user signup
class SignUpView(CreateView):
  form_class = UserCreationForm # overwriting the form with UserCreationForm
  success_url= reverse_lazy('login') # login path is built-in in Django
  template_name = 'catalog/signup.html'

class CheckedOutBooksView(LoginRequiredMixin, ListView):
  # List all BookInstances BUT I will filter based off currently logged in user session
  model = BookInstance
  template_name = 'catalog/profile.html' #overwrting the default template for listView i.e model_list.html
  paginate_by = 5 #5 book instances per page

  #overwriting the get_queryset method  
  def get_queryset(self):
    return BookInstance.objects.filter(borrower = self.request.user).all()

    # so basically self.request.user means --> when we request the template_name, it carries the user information with it, so we are making use of that information to filter out the book instaces