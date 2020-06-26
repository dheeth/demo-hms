from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    choices = (
        ('pending', 'Pending'),
        ('completed', 'Completed'))
    patient_name = models.ForeignKey(User, limit_choices_to={'groups__name': "Patients"}, on_delete=models.CASCADE, related_name="Patient")
    doctor_name = models.ForeignKey(User, limit_choices_to={'groups__name': "Doctors"}, on_delete=models.CASCADE, related_name="Doctor")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=11, choices=choices)

    def __str__(self):
        return "Appointment for " + str(self.patient_name)

class Outstanding(models.Model):
    patient_name = models.ForeignKey(User, limit_choices_to={'groups__name': "Patients"}, on_delete=models.CASCADE, related_name="Patient++")
    date = models.DateField()
    Total = models.CharField(max_length=20, null=True)
    paid = models.CharField(max_length=20, null=True)
    outstanding = models.CharField(max_length=11, null=True)

    def __str__(self):
        return "Invoice of " + str(self.patient_name)