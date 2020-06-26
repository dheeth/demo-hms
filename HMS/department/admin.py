from django.contrib import admin
from .models import Appointment, Outstanding

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Outstanding)