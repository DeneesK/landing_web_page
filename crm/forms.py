from django import forms

class OrderForms(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Name'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Phone number'}))
