import imp
from django.http import HttpResponse


from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
  return render(request, '../templates/my_app/home.html')

def my_custom_page_not_found_view(request, exception):
  return render(request, 'error_view.html', status=404)