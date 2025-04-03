# forms.py
from django import forms

class EmailForm(forms.Form):
    your_email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

   
