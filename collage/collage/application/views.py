from django.shortcuts import render,redirect
from .models import Add_hod
from .models import Add_teacher
from .models import Add_students
from .models import leave
from .models import notification
from .models import mark
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'hodregister.html')
def log(request):
    return render(request,'login.html')
def Admin(request):
    return render(request,'admin.html')
def Adhod(request):
    return render(request,'hodregister.html')
def datahod(request):
    if request.method =="POST":
        ftname=request.POST["ftname"]
        ltname=request.POST["ltname"]
        usrname=request.POST["usname"]
        addrss=request.POST["addrss"]
        plce=request.POST["plce"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        department=request.POST["department"]
        qualification=request.POST["qualification"]
        experience=request.POST["experience"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]
        role='hod'
        status='1'

        if password==confirmpassword:
            if User.objects. filter (username=usrname) .exists() :
                messages. info(request, "Username taken")
                return redirect('adhod')

            elif User.objects. filter (email=email) .exists() :
                messages. info(request, "Username taken")
                return redirect('adhod')

            else:
                user=User.objects.create_user (username=usrname, password=password)
                user. save()
            
                addhod=Add_hod(user=user,Firstname=ftname,Lastname=ltname,username=usrname,Address=addrss,place=plce,phone=phone,email=email,Department=department,qualification=qualification,experience=experience,password=password,confirmpassword=confirmpassword,role=role,status=status)
                addhod.save()
       
        else:
            return render (request,'hodregister.html')

        return redirect('adminn')
    else:
        return render(request,'hodregister.html')



def jhod(request):
    data=Add_hod.objects.all()
    return render(request,'viewhod.html',{'data':data})

def hodd (request):
    return render(request,'hodregister.html')

def delete_hod(request,hodid):
    dlthod=Add_hod.objects.get(id=hodid)
    dlthod.delete()
    return redirect('jdhod')

def HOD(request):
    return render(request,'hod.html')

def Teachers(request):
    return render(request,'teacherregister.html')

def AddTeachers(request):
    if request.method =="POST":
        hfname=request.POST["FNAME"]
        hlfname=request.POST["LNAME"]
        husrname=request.POST["UNAME"]
        haddress=request.POST["HADDRESS"]
        hplace=request.POST["HPLACE"]
        hphone=request.POST["HPHONE"]
        hemail=request.POST["HEMAIL"]
        hdepartment=request.POST["HDEPARTMENT"]
        hsubject=request.POST["HSUBJECT"]
        hqualification=request.POST["HQUALIFICATION"]
        hexperience=request.POST["HEXPERIENCE"]
        hpassword=request.POST["HPASSWORD"]
        hconfirmpassword=request.POST["HCFPASSWORD"]
        role='Teacher'
        status='0'

        if hpassword==hconfirmpassword:
            if User.objects.filter(username=husrname).exists():
                messages. info(request,"Username Taken")
                return redirect('addteachers')
            elif User.objects.filter(email=hemail).exists():
                messages. info(request,"Email Already Exists")
                return redirect('addteachers')
            else:
                user=User.objects.create_user(username=husrname,password=hpassword)
                user.save()    

                Addteacher=Add_teacher(user=user,Hfirstname=hfname,Hlastname=hlfname,Husername=husrname,Hadress=haddress,Hplace=hplace,Hphone=hphone,Hemail=hemail,Hdepartment=hdepartment,Hsubject=hsubject,Hqualification=hqualification,Hexperience=hexperience,Hpassword=hpassword,Hcpassword=hconfirmpassword,role=role,status=status)
                Addteacher.save()
        else:
            return render (request,'teacherregister.html')
        return redirect('hood')
    else:
        return render (request,'teacherregister.html')

# def VTeachers(request):
#     return render(request,'viewteacher.html')

def vteacher(request):
     collect=Add_teacher.objects.all()
     return render (request,'viewteacher.html',{"collect":collect})

def delete_teacher(request,tchid):
    dltteacher=Add_teacher.objects.get(id=tchid)
    dltteacher.delete()
    return redirect('vteacher')

def TEACHER (request):
    return render(request,'teacher.html')

def ADDSTUDENTS(request):
    return render(request,'studentregister.html')

def Addstudents(request):
    if request.method =="POST":
        sfname=request.POST["sfname"]
        slname=request.POST["slname"]
        suname=request.POST["ssuname"]
        sadress=request.POST["saddress"]
        splace=request.POST["splace"]
        sphone=request.POST["sphone"]
        semail=request.POST["semail"]
        sdepartment=request.POST["sdepartment"]
        ssubject=request.POST["ssubject"]
        sadmision=request.POST["sadm"]
        spassword=request.POST["spassword"]
        sconfirmpassword=request.POST["scpassword"]
        Srole='student'
        Sstatus='0'
        if spassword==sconfirmpassword:
            if User.objects.filter(username=suname).exists():
                messages. info(request,"Username Taken")
                return redirect('addstud')
            elif User.objects.filter(email=semail).exists():
                 messages. info(request,"Email Already Exists")
                 return redirect('addstud')
            else:
                user=User.objects.create_user(username=suname,password=spassword)
                user.save()

                Addstudents=Add_students(user=user,Sfirstname=sfname,Slastname=slname,Susername=suname,Sadress=sadress,Splace=splace,Sphone=sphone,Semail=semail,Sdepartment=sdepartment,Ssubject=ssubject,SAdmission=sadmision,Spassword=spassword,Scpassword=sconfirmpassword,Srole=Srole,Sstatus=Sstatus)
                Addstudents.save()
        else:
            return render (request,'studentregister.html')
        return redirect('addteachers')
    else:
        return render (request,'studentregister.html')
        

def vstudents(request):
    collection=Add_students.objects.all()
    return render (request,'vstudents.html',{'collection':collection})

def delete_student(request,stdid):
    dltteacher=Add_students.objects.get(id=stdid)
    dltteacher.delete()
    return redirect('vstudents')

def Adminteacher(request):
    return render(request,'adminteacher.html')

def Adminteacherview(request):
     coll=Add_teacher.objects.all()
     print("teacherrrrrrrrrrr",coll)
     return render (request,'adminteacher.html',{"coll":coll})

def Adminstudentview(request):
    list=Add_students.objects.all()
    return render (request,'adminstudent.html',{"list":list})


def delete_adminteacher(request,adtchid):
    dltteacher=Add_teacher.objects.get(id=adtchid)
    dltteacher.delete()
    return redirect('adminviewteacher')

def delete_adminstudent(request,adstid):
    dltstud=Add_students.objects.get(id=adstid)
    dltstud.delete()
    return redirect('adminstudentview')

def adminapproveteacher(request, teacher_id):
    teacherlist=Add_teacher.objects.get (id=teacher_id)
    teacherlist.status=1 
    teacherlist.save()
    return redirect ('adminviewteacher')


def adminapprovestudent(request, student_id):
    studentlist=Add_students.objects.get (id=student_id)
    studentlist.Sstatus=1 
    studentlist.save()
    return redirect ('adminstudentview')

def Adminapproveteacher(request):
    approvedteacher=Add_teacher.objects.all()
    return render (request,'adminapprovedteachers.html',{"approvedteacher":approvedteacher})

def Adminapprovestudents(request):
    approvedstudents=Add_students.objects.all()
    return render (request,'adminapprovedstudents.html',{"approvedstudents":approvedstudents})

def STUDENT(request):
    return render(request,'student.html')

#login
stat=''
rol=''
def login(request):
    global stat
    global rol
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('pass')
        print(password)

        user=authenticate(username=username,password=password)
        print("hi",user)

        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
            u_name=i['username']
            print(u_name)
            id=i['id']

            ds=Add_students.objects.filter(user_id=id).values()
            print("studentData==>",ds)
            for i in ds:
               stat=i['Sstatus']
               rol=i['Srole']
               print("Sstatus=",stat)
               print("Srole=",rol)

            dt=Add_teacher.objects.filter(user_id=id).values()
            print("teacherData==>",dt)
            for i in dt:
                stat=i['status']
                rol=i['role']
                print("status=",stat)
                print("role=",rol)
        
            dh=Add_hod.objects.filter(user_id=id).values()
            print("hodData==>",dh)
            for i in dh:
                stat=i['status']
                rol=i['role']
                print("status=",stat)
                print("role=",rol)

            if user is not None and rol=='student' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('student')

            if user is not None and rol=='Teacher' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('teacher')

            if user is not None and rol=='hod' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('hood')
            
            if user is not None and username=='admin' and password=='password':
                auth_login(request,user)
                return redirect('adminn')

        else:
            return render(request,'login.html')

    else:
        return render (request,'login.html')    


def hodprofile(request):
    if request.user:
        user=request.user
        dat=Add_hod.objects.filter(user=user).values()
        return render(request,'hodprofile.html',{'dat':dat})

def edit(request,editid):
    dat=Add_hod.objects.get(id=editid)
    return render(request,'hodprofileupdate.html',{"dat":dat})


def updateprofile(request,updateid):
    if request.method=="POST":
        update=Add_hod.objects.get(id=updateid)
        update.Firstname=request.POST["ftname"]
        update.Lastname=request.POST["ltname"]
        update.username=request.POST["usname"]
        update.Address=request.POST["addrss"]
        update.place=request.POST["plce"]
        update.phone=request.POST["phone"]
        update.email=request.POST["email"]
        update.Department=request.POST["department"]
        update.qualification=request.POST["qualification"]
        update.experience=request.POST["experience"]
        update.password=request.POST["password"]
        update.confirmpassword=request.POST["confirmpassword"]
        update.save()
        return redirect('hodprofile')

def teacherprofile(request):
    if request.user:
        user=request.user
        teach=Add_teacher.objects.filter(user=user).values()
        return render(request,'teacherprofile.html',{'teach':teach})

def teacheredit(request,techereditid):
    teach=Add_teacher.objects.get(id=techereditid)
    return render(request,'teacherprofileupdate.html',{"teach":teach})

def teacherupdateprofile(request,teacherupdateid):
    if request.method=="POST":
        teacherupdate=Add_teacher.objects.get(id=teacherupdateid)
        teacherupdate.Hfirstname=request.POST["FNAME"]
        teacherupdate.Hlastname=request.POST["LNAME"]
        teacherupdate.Husername=request.POST["UNAME"]
        teacherupdate.Hadress=request.POST["HADDRESS"]
        teacherupdate.Hplace=request.POST["HPLACE"]
        teacherupdate.Hphone=request.POST["HPHONE"]
        teacherupdate.Hemail=request.POST["HEMAIL"]
        teacherupdate.Hdepartment=request.POST["HDEPARTMENT"]
        teacherupdate.Hsubject=request.POST["HSUBJECT"]
        teacherupdate.Hqualification=request.POST["HQUALIFICATION"]
        teacherupdate.Hexperience=request.POST["HEXPERIENCE"]
        teacherupdate.Hpassword=request.POST["HPASSWORD"]
        teacherupdate.Hcpassword=request.POST["HCFPASSWORD"]
        teacherupdate.save()
        return redirect('teacherprofile')

def studentprofile(request):
    if request.user:
        user=request.user
        study=Add_students.objects.filter(user=user).values()
        return render(request,'studentprofile.html',{'study':study})

def studentedit(request,studenteditid):
    study=Add_students.objects.get(id=studenteditid)
    return render(request,'studentprofileupdate.html',{'study':study})

def studentupdateprofile(request,studentupdateid):
    if request.method=="POST":
        studentupdate=Add_students.objects.get(id=studentupdateid)
        studentupdate.Sfirstname=request.POST["sfname"]
        studentupdate.Slastname=request.POST["slname"]
        studentupdate.Susername=request.POST["ssuname"]
        studentupdate.Sadress=request.POST["saddress"]
        studentupdate.Splace=request.POST["splace"]
        studentupdate.Sphone=request.POST["sphone"]
        studentupdate.Semail=request.POST["semail"]
        studentupdate.Sdepartment=request.POST["sdepartment"]
        studentupdate.Ssubject=request.POST["ssubject"]
        studentupdate.SAdmission=request.POST["sadm"]
        studentupdate.Spassword=request.POST["spassword"]
        studentupdate.Scpassword=request.POST["scpassword"]
        studentupdate.save()
        return redirect('studentprofile')

def hodviewteachers(request):
    if request.user:
        user=request.user
        print("koo",user)
        data=Add_hod.objects.filter(user=user).values()
        for i in data:
            dept=i['Department']
        print("joo",dept)
        data1=Add_teacher.objects.filter(Hdepartment=dept).values()
        return render(request,'viewteacher.html',{'data':data1})

def teacherviewstudent(request):
    if request.user:
        user=request.user
        datas=Add_teacher.objects.filter(user=user).values()
        for i in datas:
            depat=i["Hdepartment"]
        print("shas",depat)
        datas1=Add_students.objects.filter(Sdepartment=depat)
        return render(request,'vstudents.html',{'datas':datas1})

def leafe(request):
    return render(request,'hodleave.html')

def hodleaves(request):
    if request.method =="POST":
        user=request.user
        date=request.POST["date"]
        reason=request.POST["reason"]
        status='0'
        role='hod'
        leavess=leave(user=user,date=date,reason=reason,status=status,role=role)
        leavess.save()
        data=leave.objects.all()
        return render (request,'hodleave.html',{'data':data})
    else:
        return render (request,'hodleave.html')

def tleave(request):
    return render(request,'teacherleave.html')

def teacherleaves(request):
    if request.method =="POST":
        user=request.user
        date=request.POST["date"]
        reason=request.POST["reason"]
        status='0'
        role='Teacher'
        leavess=leave(user=user,date=date,reason=reason,status=status,role=role)
        leavess.save()
        data=leave.objects.all()
        return render (request,'teacherleave.html',{'data':data})
    else:
        return render (request,'teacherleave.html')

def sleave(request):
    return render(request,'studentleave.html')

def studentleaves(request):
    if request.method =="POST":
        user=request.user
        date=request.POST["date"]
        reason=request.POST["reason"]
        status='0'
        role='student'
        leavess=leave(user=user,date=date,reason=reason,status=status,role=role)
        leavess.save()
        data=leave.objects.all()
        return render (request,'studentleave.html',{'data':data})
    else:
        return render (request,'studentleave.html')
        
def hodlview(request):
    data=Add_hod.objects.filter(role = 'hod').values()
    for i in data:
        role=i['role']
    leaves=leave.objects.filter(role=role).values()
    return render (request,'hodleaveapproval.html',{'leaves':leaves})
roles=''
dept=''
def teacherlview(request):
    global roles
    global dept
    if request.user:
        user=request.user
        print(user)
        
        data=Add_hod.objects.filter(user=user).values()
        for i in data:
            dept=i["Department"]
            print(dept)
        data1=Add_teacher.objects.filter(Hdepartment=dept).values()
        print(data1)
        for i in data1:
            roles=i['role']
            print(roles)
            leavee=leave.objects.filter (role=roles).values()
            return render(request,'teacherleaveapproval.html',{'leavee':leavee})
        else:
            return render(request,'teacherleaveapproval.html')




def studentlview(request):
    if request.user:
        user=request.user
        print(user)
        data=Add_teacher.objects.filter(user=user).values()
        for i in data:
            dept=i["Hdepartment"]
        data2=Add_students.objects.filter(Sdepartment=dept).values()
        print(data2)
        for i in data2:
            roless=i['Srole']
            leaves=leave.objects.filter(role=roless).values()
            return render(request,'studentleaveapproval.html',{'leaves':leaves})
        else:
          return render(request,'studentleaveapproval.html')


def hodlappview(request):
    data=Add_hod.objects.filter(role = 'hod').values()
    for i in data:
        id=i['user_id']
    leaves=leave.objects.filter(user=id)
    return render (request,'approved1.html',{'leaves':leaves})

def hodleavebutton(request,user_id):
    data=leave.objects.get(id=user_id)
    data.status='1'
    data.save()
    return redirect('hodleaveapproved')

def hodleavedelbutton(request,user_id):
    data=leave.objects.get(id=user_id)
    data.delete()
    return redirect('hodleaveapproved')

def teacherapplview(request):
    if request.user:
        user=request.user
        data=Add_hod.objects.filter(user=user).values()
        for i in data:
            dept=i["Department"]
        data1=Add_teacher.objects.filter(Hdepartment=dept).values()
        for i in data1:
            id=i['user_id']
        leavee=leave.objects.filter(user=id)
        return render(request,'approved2.html',{'leavee':leavee})

def teacherleavebutton(request,user_id):
    data=leave.objects.get(id=user_id)
    data.status='1'
    data.save()
    return redirect('teacherleaveapproved')

def teacherleavedelbutton(request,user_id):
    data=leave.objects.get(id=user_id)
    data.delete()
    return redirect('teacherleaveapproved')

def studentapplview(request):
    if request.user:
        user=request.user
        data=Add_teacher.objects.filter(user=user).values()
        for i in data:
            deept=i["Hdepartment"]
        data2=Add_students.objects.filter(Sdepartment=deept).values()
        for i in data2:
            id=i['user_id']
        leaves=leave.objects.filter(user=id)
        return render(request,'approved3.html',{'leavess':leaves})

def studentleavebutton(request,user_id):
    data=leave.objects.get(id=user_id)
    data.status='1'
    data.save()
    return redirect('studentleaveapproved')

def studentleavedelbutton(request,user_id):
    data=leave.objects.get(id=user_id)
    data.delete()
    return redirect('studentleaveapproved')

def Notification(request):
    if request.method =="POST":
        user=request.user
        date=request.POST["date"]
        notificationss=request.POST["notification"]
        status='0'
        role=''
        department=request.POST["department"]
        Nootifications=notification(user=user,date=date,notification=notificationss,status=status,role=role,department=department)
        Nootifications.save()
        data=notification.objects.all()
        return render (request,'exam1.html',{'data':data})
    else:
        return render (request,'exam1.html')

def Notificationview(request):
    if request.user:
        user=request.user
        dept=''
        data=Add_hod.objects.filter(user=user).values()
        for i in data:
            dept=i["Department"]
        datas=notification.objects.filter(department=dept)
        return render (request,'exam.html',{'data':datas})

def Notificationapproveview(request):
    if request.user:
        user=request.user
        dept=''
        data=Add_hod.objects.filter(user=user).values()
        for i in data:
            dept=i["Department"]
        datas=notification.objects.filter(department=dept)
        return render (request,'exam2.html',{'data':datas})


def Notificationapproved(request,user_id):
    datas=notification.objects.get(id=user_id)
    datas.status='1'
    datas.save()
    return redirect ('Notificationapproveview')

def markupload(request):
    return render(request,"mark.html")    

def publish(request):
    if request.user:
        user=request.user
        print("bvjkdsf",user)
        if request.method =="POST":
            department=request.POST["department"]
            subject=request.POST["subject"]
            total=request.POST["total"]
            mymark=request.POST["mymark"]
            status='0'
            result=mark(user=user,department=department,subject=subject,total=total,mymark=mymark,status=status)
            result.save()
            print("jdbjnb",mymark)
            return render (request,'mark.html')
        else:
             return render(request,'mark.html')

def publishview(request):
    if request.user:
        user=request.user
        dept=''
        sub=''
        data=Add_students.objects.filter(user=user).values()
        for i in data:
            dept=i["Sdepartment"]
            sub=i["Ssubject"]
        dataas=mark.objects.filter(Q(department=dept) & Q(subject=sub))
        return render (request,'mark2.html',{'data':dataas})

