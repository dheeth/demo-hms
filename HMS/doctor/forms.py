from django.forms import ModelForm
from .models import Prescription, Doctor

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['doctor_name']

class DoctorProfile(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user','attendence','salary','status']