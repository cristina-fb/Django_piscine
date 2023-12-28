from django import forms

class MyForm(forms.Form):
    email = forms.CharField(label="ENTER YOUR E-MAIL HERE", max_length=100)