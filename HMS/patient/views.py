from django.shortcuts import render, redirect
from django.contrib import messages
from department.models import Appointment, Outstanding
from doctor.models import Prescription
from .forms import PatientProfile
from django.contrib.auth import logout

# Create your views here.

def home(request):
    user = request.user
    context = {'user': user}
    return render(request, 'patient/Home.html', context)

def appointments(request):
    appointment = Appointment.objects.filter(patient_name=request.user)
    context = {'appointment': appointment}
    return render(request, 'patient/appointments.html', context)

def invoices(request):
    invoice = Outstanding.objects.filter(patient_name=request.user)
    context = {'invoice': invoice}
    return render(request, 'patient/invoices.html', context)

def profile(request):
    patient = request.user.patient
    form = PatientProfile(instance=patient)
    if request.method == 'POST':
        form = PatientProfile(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Information Updated")
            return redirect('/patient/profile')
    context = {'form': form}
    return render(request, 'patient/profile.html', context)

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')

def history(request):
    prescribe = Prescription.objects.filter(patient_name=request.user)
    context = {'prescribe': prescribe}
    return render(request, 'patient/history.html', context)