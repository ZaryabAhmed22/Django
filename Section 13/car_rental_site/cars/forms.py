from dataclasses import field
from django import forms
from .models import ReviewModel
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#   first_name = forms.CharField(label="First Name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control no-border'}))
#   last_name = forms.CharField(label="Last Name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control no-border'}))
#   email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control no-border'}))
#   review = forms.CharField(label='Please write your review', widget=forms.Textarea(attrs={'class': 'form-control no-border'}))


# Creating a model form
class ReviewForm(ModelForm):
  class Meta:
    model = ReviewModel
    fields = ['first_name', 'last_name', 'stars'] # fields="__all__"

    labels = {
      'first_name': "YOUR FIRST NAME",
      'last_name': "YOUR LAST NAME",
      'stars': "RATING",
    }