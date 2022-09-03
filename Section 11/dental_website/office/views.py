from django.shortcuts import render
from . import models

# Create your views here.
def list_patients(request):
  all_patients = models.Patient.objects.all()
  context_list = {'patients': all_patients} # the data to be used, refer section 10

  return render(request,'office/list.html', context=context_list)