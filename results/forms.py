from django.forms import ModelForm
from django import forms
from .models import DeclareResult

class DeclareResultForm(ModelForm):
    class Meta:
        model = DeclareResult
        fields = ['select_class', 'select_student']
        widgets = {
            'select_class': forms.Select(attrs={'class': 'form-control'}),
            'select_student':  forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'select_class' : 'Class',
            'select_student' : 'Select Student',
        }
