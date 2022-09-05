from django import forms

class ReviewForm(forms.Form):
  first_name = forms.CharField(label="First Name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(label="Last Name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
  review = forms.CharField(label='Please write your review', widget=forms.TextInput(attrs={'class': 'form-control'}))