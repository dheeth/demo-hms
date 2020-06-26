from django.forms import ModelForm
from django import forms
from .models import Patient

class PatientProfile(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']