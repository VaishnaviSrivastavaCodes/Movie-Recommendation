from django import forms

class SearchForm(forms.Form):
    title = forms.CharField()