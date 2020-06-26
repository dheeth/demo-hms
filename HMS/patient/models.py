from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female'))
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, limit_choices_to={'groups__name':'Patients'})
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=100, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, null=True)
    age = models.CharField(max_length=3, null=True)
    address = models.CharField(max_length=255, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    medical_reports = models.FileField(null=True, blank=True)
    case_paper = models.CharField(max_length=13, null=True)

    def __str__(self):
        return self.user.username
    
