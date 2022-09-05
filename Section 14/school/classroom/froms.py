from email import message
from socket import fromshare
from django import forms

class ContactForm(forms.Form):
  name = forms.CharField()
  message = forms.CharField(widget=forms.Textarea)