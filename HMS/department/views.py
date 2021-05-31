from django.shortcuts import render, redirect
from .models import Appointment, Outstanding
from .forms import AppointmentForm
from django.contrib.auth import logout
from django.db.models import Sum
from django.contrib import messages
from patient.models import Patient
from doctor.models import Doctor
from patient.forms import PatientProfile

# Create your views here.
from .forms import AppointmentForm, UpdateDoctor

def redashboard(request):
    appointments = Appointment.objects.all()
    total_appointments = appointments.count()
    done = Appointment.objects.filter(status='completed')
    appointments_done = done.count()
    pending = Appointment.objects.filter(status='pending')
    appointments_pending = pending.count()
    patients = Patient.objects.all()
    context = {'appointments': appointments, 'total_appointments': total_appointments, 'appointments_done': appointments_done, 'appointments_pending': appointments_pending, 'patients': patients}
    return render(request, 'department/redashboard.html', context)

def hrdashboard(request):
    doctors = Doctor.objects.all()
    duty_doctors = Doctor.objects.filter(status='Active')
    patients = Patient.objects.all()
    total_doctors = doctors.count()
    total_patients = patients.count()
    on_duty_doctors = duty_doctors.count()
    context = {'total_doctors': total_doctors, 'total_patients': total_patients, 'on_duty_doctors': on_duty_doctors, 'doctors': doctors}
    return render(request, 'department/hrdashboard.html', context)

def accounts(request):
    outstandings = Outstanding.objects.values('patient_name__first_name').order_by('patient_name__first_name').annotate(unpaid=Sum('outstanding'), paid=Sum('paid'))
    total_outstandings = Outstanding.objects.all()
    context = {'outstandings': outstandings, 'total_outstandings': total_outstandings}
    return render(request, 'department/accounts.html', context)

def createAppointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/department/reception-dashboard')
    context = {'form': form}
    return render(request, 'department/create-appointment.html', context)

def updateAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/department/reception-dashboard')
    context = {'form': form}
    return render(request, 'department/update-appointment.html', context)



def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')

def createPatient(request):
    form = PatientProfile()
    if request.method == 'POST':
        form = PatientProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/department/reception-dashboard')
    context = {'form': form}
    return render(request, 'patient/profile.html', context)

def updatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientProfile(instance=patient)
    if request.method == 'POST':
        form = PatientProfile(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/department/reception-dashboard')
    context = {'form': form}
    return render(request, 'department/update-patient.html', context)

def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('/department/reception-dashboard')
    context = {'item': patient}
    return render(request, 'department/delete.html', context)

def updateDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = UpdateDoctor(instance=doctor)
    if request.method == 'POST':
        form = UpdateDoctor(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/department/hrdashboard')
    context = {'form': form}
    return render(request, 'department/update-doctor.html', context)

def deleteDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('/department/hrdashboard')
    context = {'item': doctor}
    return render(request, 'department/delete.html', context)