from django.forms import ModelForm
from django import forms
from .models import StudentClass

class StudentClassForm(ModelForm):
    class Meta:
        model = StudentClass
        exlude  =   'creation_date'
        fields = '__all__'
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_name_in_numeric':  forms.NumberInput(attrs={'class': 'form-control'}),
            'section':  forms.TextInput(attrs={'class': 'form-control'}),
        }