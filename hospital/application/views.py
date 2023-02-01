from django.shortcuts import render,redirect
from .models import Doctorregistration
from .models import Patientregistration
from .models import Booking
from .models import Medicine
from .models import Leave
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def home(request):
    return render(request,"home.html")
def admin(request):
    return render(request,"admin.html")
def login(request):
    return render(request,"login.html")
def doctor(request):
    return render(request,"doctor.html")
def doctorreg(request):
    return render(request,"doctorregistration.html")
def patientreg(request):
    return render(request,"patientregister.html")
def patient(request):
    return render(request,"patient.html")

def addingdoctor(request):
    if request.user:
        user=request.user
    if request.method =="POST":
        fullname=request.POST["fullname"]
        username=request.POST["username"]
        email=request.POST["email"]
        specialised=request.POST["specialised"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]
        status='1'
        role='Doctor'
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect("addingdoctor")
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,'username taken')
            #     return redirect("addingdoctor")
            else:
                user=User.objects.create_user (username=username, password=password)
                user. save()
                registration1=Doctorregistration(user=user,fullname=fullname,username=username,email=email,specialised=specialised,password=password,confirmpassword=confirmpassword,status=status,role=role)
                registration1.save()
        else:
            return render(request,'doctorregistration.html')
        return redirect('main')
    else:
        return render(request,'doctorregistration.html')

def addingpatient(request):
    if request.user:
        user=request.user
    if request.method=="POST":
        fullname=request.POST["fullname"]
        username=request.POST["username"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        district=request.POST["district"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]
        status='1'
        role='Patient'
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect("addingpatient")
            else:
                user=User.objects.create_user (username=username, password=password)
                user. save()
                registration1=Patientregistration(user=user,fullname=fullname,username=username,email=email,phone=phone,address=address,district=district,password=password,confirmpassword=confirmpassword,status=status,role=role)
                registration1.save()
        else:
            return render(request,'patientregister.html')
        return redirect('home')
    else:
        return render(request,'patientregister.html')




def login(request):
    global stat
    global rol

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        print("hi",user)

        data=User.objects.filter(username=username).values()
        for i in data:
            u_name=i["username"]
            print(u_name)
            id=i['id']
            data1=Doctorregistration.objects.filter(user_id=id).values()
            data2=Patientregistration.objects.filter(user_id=id).values()
            for i in data1:
                rol=i["role"]
                stat=i["status"]
            for i in data2:
                rol=i["role"]
                stat=i["status"]
            if user is not None and username=='admin' and password=='password':
                auth_login(request,user)
                return redirect('main')  
            if user is not None and rol=='Doctor' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('doctor')
            if user is not None and rol=='Patient' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('patient')

        else:
            return render(request,'login.html')      
    else:
        return render(request,'login.html')
        
def doctorprofile(request):
    if request.user:
        user=request.user
        dat=Doctorregistration.objects.filter(user=user).values()
        return render(request,'Doctorprofile.html',{'dat':dat})

def doctoreditprofile(request,doctoreditid):
    dat=Doctorregistration.objects.get(id=doctoreditid)
    return render (request,'Doctorprofileupdate.html',{"dat":dat})

def doctorprofileupdate(request,doctorupdateid):
    if request.method=='POST':
        update=Doctorregistration.objects.get(id=doctorupdateid)
        update.fullname=request.POST["fullname"]
        update.username=request.POST["username"]
        update.email=request.POST["email"]
        update.specialised=request.POST["specialised"]
        update.password=request.POST["password"]
        update.confirmpassword=request.POST["confirmpassword"]
        update.save()
        return redirect('doctorprofile')

def patientprofile(request):
    if request.user:
        user=request.user
        data=Patientregistration.objects.filter(user=user).values()
        return render(request,'Patientprofile.html',{'data':data})

def patienteditprofile(request,patienteditid):
    data=Patientregistration.objects.get(id=patienteditid)
    return render (request,'Patientprofileupdate.html',{"data":data})

def patientprofileupdate(request,patientupdateid):
    if request.method=='POST':
        update=Patientregistration.objects.get(id=patientupdateid)
        update.fullname=request.POST["fullname"]
        update.username=request.POST["username"]
        update.email=request.POST["email"]
        update.phone=request.POST["phone"]
        update.address=request.POST["address"]
        update.district=request.POST["district"]
        update.password=request.POST["password"]
        update.confirmpassword=request.POST["confirmpassword"]
        update.save()
        return redirect('patientprofile')

def booking(request):
    if request.method=="POST":
        user=request.user
        department=request.POST["department"]
        doctorr=request.POST["doctor"]
        date=request.POST["date"]
        status='0'
        Bookings=Booking(user=user,department=department,doctor=doctorr,date=date,status=status)
        Bookings.save()
        dataa=Booking.objects.all()
        return render (request,'booking.html',{'dataa':dataa})
    else:
         return render (request,'booking.html')


def bookingview(request):
    data=Booking.objects.all()
    return render(request,'bookingview.html',{'data':data})

def bookingapprove(request,user_id):
    bookinglist=Booking.objects.get(id=user_id)
    bookinglist.status=1
    bookinglist.save()
    return redirect('bookingapprovedview')

def bookingreject(request,user_id):
    bookinglist=Booking.objects.get(id=user_id)
    bookinglist.delete()
    return redirect('main')

def bookingapprovedview(request):
    if request.user:
        user=request.user
        depat=''
    data=Doctorregistration.objects.filter(user=user).values()
    for i in data:
        depat=i["specialised"]
    datas=Booking.objects.filter(department=depat)
    return render(request,'bookingapprovedview.html',{'data':datas})

def prescription(request):
    if request.method=="POST":
        user=request.user
        name=request.POST["name"]
        age=request.POST["age"]
        gender=request.POST["gender"]
        date=request.POST["date"]
        diagnosis=request.POST["diagnosis"]
        drugname=request.POST["drugname"]
        status='0'
        presription=Medicine(user=user,name=name,age=age,gender=gender,date=date,diagnosis=diagnosis,drugname=drugname,status=status)
        presription.save()
        datas=Medicine.objects.all()
        return render (request,'prescription.html',{'data':datas})
    else:
        return render (request,'prescription.html')


def prescriptionview(request):
    if request.user:
        user=request.user
        namess=''
    data1=Patientregistration.objects.filter(user=user).values()
    for i in data1:
        namess=i["fullname"]
    datas=Medicine.objects.filter(name=namess)
    return render(request,"Prescriptionview.html",{'data':datas})

# def leave(request):
#     return render(request,"doctorleave.html")

def leaveapply(request):
    if request.method=="POST":
        user=request.user
        date=request.POST["date"]
        reason=request.POST["reason"]
        status='0'
        leaves=Leave(user=user,date=date,reason=reason,status=status)
        leaves.save()
        datas=Leave.objects.all()
        return render (request,'doctorleave.html',{'data':datas})
    else:
        return render (request,'doctorleave.html')
    
def leaveview(request):
    data=Leave.objects.all()
    return render(request,'doctorleaveview.html',{'data':data})

def leaveapproved(request,user_id):
    leavelist=Leave.objects.get(id=user_id)
    leavelist.status=1
    leavelist.save()
    return redirect('leaveapprovedview')

def leaveapprovedview(request):
    data=Leave.objects.all()
    return render(request,'doctorleaveapprovedview.html',{'data':data})