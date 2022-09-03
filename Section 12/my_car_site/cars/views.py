from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list(request):
  all_cars = models.Car.objects.all()
  context = {'all_cars': all_cars}
  return render(request,'cars/list.html', context=context)

def add(request):
  print(request.POST)
  if(request.method =='POST'):
    brand = request.POST['brand']
    year = int(request.POST['year'])
    models.Car.objects.create(brand=brand, year=year)
    return redirect(reverse('cars:list'))
  else:
    return render(request, 'cars/add.html') 

def delete(request):
  return render(request, 'cars/delete.html')