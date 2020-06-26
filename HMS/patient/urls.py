from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='patientHome'),
    path('appointments', views.appointments, name='patientAppoint'),
    path('payments', views.invoices, name='patientInvoices'),
    path('profile', views.profile, name='patientProfile'),
    path('history', views.history, name='patientHistory'),
    path('logout', views.handleLogout, name='handleLogout'),
]