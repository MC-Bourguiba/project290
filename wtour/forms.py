from django import forms

class NumForm(forms.Form):
    cities = forms.CharField(label='How many cities do you want to visit?', max_length=100)
    departure = forms.CharField(label='Departure', max_length=100)
