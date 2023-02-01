"""collage URL Configuration

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

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('log', views.log, name='login'),
    path('adminn',views.Admin,name='adminn'),
    path('adhod',views.Adhod,name='adhod'),
    path('datahod',views.datahod,name='dthod'),
    path('chod',views.jhod,name='jdhod'),
    path('vhod',views.hodd,name='hhh'),
    path('delete_hod/<int:hodid>',views.delete_hod,name='delete_hod'),
    path('HOD',views.HOD,name='hood'),
    path('teachers',views.Teachers,name='addteachers'),
    path('addteacher',views.AddTeachers,name='addteacher'),
    # path('vteachers',views.VTeachers,name='viewteachers'),
    path('vvteacher',views.hodviewteachers,name='vteacher'),
    path('delete_teacher/<int:tchid>',views.delete_teacher,name='delete_teacher'),
    path('teacher',views.TEACHER,name='teacher'),
    path('addstd',views.ADDSTUDENTS,name='addstud'),
    path('addstudents',views.Addstudents,name='addstudents'),
    path('vstudents',views.teacherviewstudent,name='vstudents'),
    path('delete_student/<int:stdid>',views.delete_student,name='delete_student'),
    path('adminteacher',views.Adminteacher,name='adminteacher'),
    path('vadminteacher',views.Adminteacherview,name='adminviewteacher'),
    path('vadminstudent',views.Adminstudentview,name='adminstudentview'),
    path('delete_adminteacher/<int:adtchid>',views.delete_adminteacher,name='delete_adminteacher'),
    path('delete_adminstudent/<int:adstid>',views.delete_adminstudent,name='delete_adminstudent'),
    path('approveteacher/int:<teacher_id>',views.adminapproveteacher,name='approveteracher'),
    path('approvestudent/int:<student_id>',views.adminapprovestudent,name='approvestudent'),
    path('approvedteachers',views.Adminapproveteacher,name='approvedteachers'),
    path('approvedstudents',views.Adminapprovestudents,name='approvedstudents'),
    path('student',views.STUDENT,name='student'),
    path('loggin',views.login,name='loggin'),
    path('hodprofile',views.hodprofile, name='hodprofile'),
    path('edit/<int:editid>',views.edit,name='edit'),
    path('<int:updateid>/update',views.updateprofile,name='update'),
    path('teacherprofile',views.teacherprofile, name='teacherprofile'),
    path('teacheredit/<int:techereditid>',views.teacheredit,name='teacheredit'),
    path('<int:teacherupdateid>/teacherupdate',views.teacherupdateprofile,name='teacherupdate'),
    path('studentprofile',views.studentprofile, name='studentprofile'),
    path('studentedit/<int:studenteditid>',views.studentedit,name='studentedit'),
    path('<int:studentupdateid>/studentupdate',views.studentupdateprofile,name='studentupdate'),
    path('leafe',views.leafe,name="leafe"),
    path('hodleave',views.hodleaves,name="hodleaves"),
    path('tleave',views.tleave,name="tleave"),
    path('teacherleave',views.teacherleaves,name="teacherleaves"),
    path('sleave',views.sleave,name="sleave"),
    path('studentleaves',views.studentleaves,name="studentleaves"),
    path('hodleaveapproval',views.hodlview,name="hodleaveapproval"),
    path('teacherleafe',views.teacherlview,name="teacherleafe"),
    path('studentleafe',views.studentlview,name="studentleafe"),
    path('hodleaveapproved',views.hodlappview,name="hodleaveapproved"),
    path('hodleaveok/int:<user_id>',views.hodleavebutton,name='hodleaveok'),
    path('hoddeleteok/int:<user_id>',views.hodleavedelbutton,name='hoddeleteok'),
    path('teacherleaveapproved',views.teacherapplview,name="teacherleaveapproved"),
    path('teacherleaveok/int:<user_id>',views.teacherleavebutton,name='teacherleaveok'),
    path('teachedeleteok/int:<user_id>',views.teacherleavedelbutton,name='teachedeleteok'),
    path('studentleaveapproved',views.studentapplview,name="studentleaveapproved"),
    path('studentleaveok/int:<user_id>',views.studentleavebutton,name='studentleaveok'),
    path('studentleavedelbutton/int:<user_id>',views.studentleavedelbutton,name='studentleavedelbutton'),
    path('notification',views.Notification,name="notification"),
    path('notificationview',views.Notificationview,name="notificationview"),
    path('Notificationapproveview',views.Notificationapproveview,name="Notificationapproveview"),
    path('notificationapprove/int:<user_id>',views.Notificationapproved,name='notificationapprove'),
    path('publish',views.publish,name="publish"),
    path('markupload',views.markupload,name="markupload"),
    path('publishview',views.publishview,name="publishview"),
]
