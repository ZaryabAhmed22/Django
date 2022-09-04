from django.shortcuts import render, redirect
from django.urls import reverse
from cars.forms import ReviewForm

# Create your views here.
def rental_review(request):

  # POST REQUEST --> FORM CONTENTS --> THANK YOU
  if request.method == 'POST':
    form = ReviewForm(request.POST) # Creating a form instance and populating it with the post rquest

    #Checking if the form is valid
    if form.is_valid():
      #{''first_name; 'JOSE',}
      print(form.cleaned_data) #cleaned_data is a python dictionary 

      #redirecting the user to thankyou
      return redirect(reverse('cars:thank_you'))
  else:
    form = ReviewForm()
  return render(request, 'cars/rental_review.html', context={'form': form})

def thank_you(request):
  return render(request, 'cars/thank_you.html')
