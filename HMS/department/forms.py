from django.forms import ModelForm
from .models import Appointment
from doctor.models import Doctor

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class UpdateDoctor(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user']