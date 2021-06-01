from django import forms
from django.forms import ModelForm
from .models import Gen_info, Developer, Package

class GForm(ModelForm):
    class Meta:
        model = Gen_info
        fields = '__all__'
        labels = {
        'name': '',
        'launched': '',
        'clock_rate': '',
        'bit': '',
        'developer': 'developer name',
        'package': 'package name',
        }
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
        'launched': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'launched(year)'}),
        'clock_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'clock rate Hz'}),
        'bit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'bits'}),
        'developer': forms.Select(attrs={'class': 'form-control', 'placeholder': 'developer name'}),
        'package': forms.Select(attrs={'class': 'form-control', 'placeholder': 'package name'}),
        }


class DForm(ModelForm):
    class Meta:
        model = Developer
        fields = ('dev_name',)
        labels = {
        'dev_name': '',
        }
        widgets = {
        'dev_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Developer name'})
        }

class PForm(ModelForm):
    class Meta:
        model = Package
        fields = ('pack_name',)
        labels = {
        'pack_name': '',
        }
        widgets = {
        'pack_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Package name'})
        }