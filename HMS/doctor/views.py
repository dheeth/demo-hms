from django.shortcuts import render, redirect
from department.models import Appointment
from django.contrib import messages
from .models import Prescription
from .forms import PrescriptionForm
from django.contrib.auth import logout

# Create your views here.
from .forms import DoctorProfile

def home(request):
    return render(request, 'doctor/Home.html')

def appointments(request):
    appointment = Appointment.objects.filter(doctor_name=request.user)
    context = {'appointment': appointment}
    return render(request, 'doctor/appointments.html', context)

def profile(request):
    doctor = request.user.doctor
    form = DoctorProfile(instance=doctor)
    if request.method == 'POST':
        form = DoctorProfile(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Information Updated")
            return redirect('/doctor/profile')
    context = {'form': form}
    return render(request, 'doctor/profile.html', context)

def prescriptions(request):
    prescribe = Prescription.objects.filter(doctor_name=request.user)
    context = {'prescribe': prescribe}
    return render(request, 'doctor/prescriptions.html', context)

def createPrescription(request):
    form = PrescriptionForm()
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.doctor_name = request.user
            save_form.save()
            return redirect('/doctor/prescriptions')
    context = {'form': form}
    return render(request, 'doctor/create-prescription.html', context)

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')