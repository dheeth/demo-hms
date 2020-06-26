from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from patient.models import Patient
from doctor.models import Doctor

def home(request):
    return render(request, 'management/home.html')

def about(request):
    return render(request, 'management/about.html')

def contact(request):
    return render(request, 'management/contact.html')

def register(request):
    return render(request, 'management/register.html')

def handleSignup(request):
    try:
        if request.method == 'POST':
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            username = request.POST['uname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            registerType = request.POST['registerType']
            if len(username) > 15:
                messages.error(request, "Username must be less then 15 characters")
                return redirect('/register')
            if pass1 != pass2:
                messages.error(request, "Passwords do not match")
                return redirect('/register')
            if not username.isalnum():
                messages.error(request, "Username should have letters and numbers only")
                return redirect('/register')
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = first_name
            myuser.last_name = last_name
            user = myuser.save()
            if registerType == 'Patient':
                patientGroup = Group.objects.get_by_natural_key('Patients')
                myuser.groups.add(patientGroup)
                Patient.objects.create(
                    user=myuser,
                    first_name=first_name,
                    last_name=last_name,
                    email=email

                )
            elif registerType == 'Doctor':
                doctorGroup = Group.objects.get_by_natural_key('Doctors')
                myuser.groups.add(doctorGroup)
                Doctor.objects.create(
                    user=myuser,
                    first_name=first_name,
                    last_name=last_name,
                    email=email

                )

            messages.success(request, "Your account has been successfully created")
            return redirect('/signin')
    except Exception as e:
        if "auth_user.username" in str(e):
            messages.error(request, "Username already exists, please try a unique one")
            return redirect('/register')
        else:
            return HttpResponse("404 - Not Found")
    

def signin(request):
    return render(request, 'management/login.html')

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        password = request.POST['loginpass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            group = request.user.groups.filter(user=request.user)[0]
            if group.name == "Patients":
                return redirect('/patient/appointments')
            elif group.name == "Doctors":
                return redirect('/doctor/appointments')
            elif group.name == "Reception":
                return redirect('/department/reception-dashboard')
            elif group.name == "HR":
                return redirect('/department/hrdashboard')
        else:
            messages.error(request, "Invalid username or password, Please try again")
            return redirect('/signin')
    else:
        return HttpResponse("404 - Not Found")