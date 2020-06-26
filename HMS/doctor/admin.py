from django.contrib import admin
from .models import Prescription, Doctor

# Register your models here.

admin.site.register(Prescription)
admin.site.register(Doctor)