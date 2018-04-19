from django import forms

class NumForm(forms.Form):
    cities = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Number of cities'}))
    departure = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Departure'}))
