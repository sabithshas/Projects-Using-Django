"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name="home"),
    path('main',views.admin,name="main"),
    path('login',views.login,name="login"),
    path('doctor',views.doctor,name="doctor"),
    path('doctorreg',views.doctorreg,name="doctorreg"),
    path('addingdoctor',views.addingdoctor,name="addingdoctor"),
    path('login',views.login,name="login"),
    path('patientreg',views.patientreg,name="patientreg"),
    path('addingpatient',views.addingpatient,name="addingpatient"),
    path('patient',views.patient,name="patient"),
    path('doctorprofile',views.doctorprofile,name="doctorprofile"),
    path('patientprofile',views.patientprofile,name="patientprofile"),
    path('doctoreditid/<int:doctoreditid>',views.doctoreditprofile,name='doctoreditid'),
    path('doctorupdateid/<int:doctorupdateid>',views.doctorprofileupdate,name='doctorupdateid'),
    path('patienteditid/<int:patienteditid>',views.patienteditprofile,name='patienteditid'),
    path('patientupdateid/<int:patientupdateid>',views.patientprofileupdate,name='patientupdateid'),
    path('booking',views.booking,name="booking"),
    path('bookingview',views.bookingview,name="bookingview"),
    path('bookingapproved/int:<user_id>',views.bookingapprove,name='bookingapproved'),
    path('bookingreject/int:<user_id>',views.bookingreject,name='bookingreject'),
    path('bookingapprovedview',views.bookingapprovedview,name="bookingapprovedview"),
    path('prescription',views.prescription,name="prescription"),
    path('prescriptionview',views.prescriptionview,name="prescriptionview"),
    path('leave',views.leaveapply,name="leave"),
    path('leaveview',views.leaveview,name="leaveview"),
    path('leaveapproved/int:<user_id>',views.leaveapproved,name='leaveapproved'),
    path('leaveapprovedview',views.leaveapprovedview,name="leaveapprovedview"),

] + static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
