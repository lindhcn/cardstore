from .models import Card
from django.forms import ModelForm
from django import forms

# declaring the ModelForm
class EditcardForm(ModelForm):
    
    class Meta:
        # the Model from which the form will inherit from
        model = Card
        # the fields we want from the Model
        fields = '__all__'
        # styling the form with bootstrap classes
        widgets = {
             'player': forms.TextInput(attrs={'class': 'form-control'}),
             'series': forms.TextInput(attrs={'class': 'form-control'}),
             'year': forms.TextInput(attrs={'class': 'form-control'}),
             'index': forms.TextInput(attrs={'class': 'form-control'}),
             'image': forms.TextInput(attrs={'class': 'form-control'}),
        }
