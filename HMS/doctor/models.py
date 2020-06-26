from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prescription(models.Model):
    patient_name = models.ForeignKey(User, limit_choices_to={'groups__name': "Patients"}, on_delete=models.CASCADE, related_name="Patient+")
    doctor_name = models.ForeignKey(User, limit_choices_to={'groups__name': "Doctors"}, on_delete=models.CASCADE, related_name="Doctor+")
    date = models.DateField(auto_now=True)
    prescription = models.CharField(max_length=255)
    diseases = models.CharField(max_length=150)

    def __str__(self):
        return "Prescription for " + str(self.patient_name)

class Doctor(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'))

    DEPARTMENT_CHOICES = (
        ('Oncology', 'Oncology'),
        ('Neurology', 'Neurology'),
        ('OPD', 'OPD'))

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'))

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, limit_choices_to={'groups__name':'Doctors'})
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=100, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, null=True)
    age = models.CharField(max_length=3, null=True)
    address = models.CharField(max_length=255, null=True)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=128, null=True)
    attendence = models.CharField(max_length=100, null=True)
    salary = models.CharField(max_length=128, null=True)
    status = models.CharField(choices=STATUS, max_length=128, null=True)

    def __str__(self):
        return self.user.username