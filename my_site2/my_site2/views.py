import imp
from django.http import HttpResponse


from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
  return HttpResponse("HOME_PAGE")