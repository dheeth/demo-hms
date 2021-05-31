from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='departmentHome'),
    # path('about', views.about, name='departmentAbout'),
    path('reception-dashboard', views.redashboard, name='redashboard'),
    path('hrdashboard', views.hrdashboard, name='hrdashboard'),
    path('accounts', views.accounts, name='accounts'),
    path('create-appointment', views.createAppointment, name='createAppointment'),
    path('update-appointment/<str:pk>/', views.updateAppointment, name='updateAppointment'),
    path('create-patient', views.createPatient, name='createPatient'),
    path('update-patient/<str:pk>/', views.updatePatient, name='updatePatient'),
    path('delete-patient/<str:pk>/', views.deletePatient, name='deletePatient'),
    path('update-doctor/<str:pk>/', views.updateDoctor, name='updatePatient'),
    path('delete-doctor/<str:pk>/', views.deleteDoctor, name='deletePatient'),
    path('logout', views.handleLogout, name='handleLogout'),
    # path('contact', views.contact, name='departmentContact'),
]