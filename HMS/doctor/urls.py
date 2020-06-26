from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='doctorHome'),
    path('appointments', views.appointments, name='doctorAppoint'),
    path('prescriptions', views.prescriptions, name='doctorPrescribe'),
    path('create-prescription', views.createPrescription, name='createPrescription'),
    path('profile', views.profile, name='doctorProfile'),
    path('logout', views.handleLogout, name='handleLogout'),
]