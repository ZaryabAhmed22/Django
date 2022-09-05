from django import forms

class ReviewForm(forms.Form):
  first_name = forms.CharField(label="First Name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control no-border'}))
  last_name = forms.CharField(label="Last Name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control no-border'}))
  email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control no-border'}))
  review = forms.CharField(label='Please write your review', widget=forms.Textarea(attrs={'class': 'form-control no-border'}))