from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.core.mail import EmailMessage
from itertools import count

from django.db.models import Q, Sum
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse

from models import Employee, managermodel, adminmodel

<<<<<<< HEAD
def htmlpage(request):
    return render(request, 'index.html')
=======
# def hello_world(request):
    #return HttpResponse("Hello, world!")

# ----- Manager -----

def managerRegistration(request):
    return render(request, "manager.html")

def saveManager(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['phone']
    gender = request.POST['gender']
    bloodGroup = request.POST['bloodGroup']
    dob=request.POST['dob']
    address = request.POST['address']
    state=request.POST['state']
    qualification=request.POST['qualification']
    emailId = request.POST['email']
    password = request.POST['password']
    image = request.FILES['image']
    resume = request.FILES['resume']

    e = managermodel(fname=fname, lname=lname, phone=phone, gender=gender,bloodGroup=bloodGroup,
                 dob=dob, address=address, state=state,  qualification=qualification,
                 emailId=emailId, password=password, image=image, resume=resume)
    e.save()
    if e:
        msg = "Your Application has been Submited. We will Back to you Soon"
        return render(request, "manager.html", {'msg': msg})
    else:
        return HttpResponse("error")

def managerLogin(request):
    return render(request, "managerLogin_.html")

def loginManager(request):
    emailId = request.POST['email']
    password = request.POST['password']
    c = managermodel.objects.filter(emailId=emailId, password=password,account='Active')
    if c:
        request.session['mngid'] = c[0].managerCode
        request.session['managerFname'] = c[0].fname
        request.session['managerLname'] = c[0].lname
        date = datetime.now().date()
        return HttpResponseRedirect(reverse("managerDashboard"))
    else:
        msg = 'You Are Not Valid User'
        return render(request, "managerLogin.html", {'msg': msg})

# ----- Employee -----
    
def employeeRegistration(request):
    return render(request, "employeeReg.html")

def saveEmployee(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['phone']
    gender = request.POST['gender']
    bloodGroup = request.POST['bloodGroup']
    dob=request.POST['dob']
    address = request.POST['address']
    state=request.POST['state']
    qualification=request.POST['qualification']
    emailId = request.POST['email']
    password = request.POST['password']
    image = request.FILES['image']
    resume = request.FILES['resume']
    
    e = Employee(fname=fname, lname=lname, phone=phone, gender=gender,bloodGroup=bloodGroup,
                 dob=dob, address=address, state=state,  qualification=qualification,
                 emailId=emailId, password=password, image=image, resume=resume)
    e.save()
    if e:
        msg = "Your Application has been Submited. We will Back to you Soon"
        return render(request, "employeeRegistration.html", {'msg': msg})
    else:
        return HttpResponse("error")

def employeeLogin(request):
    return render(request, "employeeLogin_.html")

def loginEmployee(request):
    emailId = request.POST['email']
    password = request.POST['password']
    c = Employee.objects.filter(emailId=emailId, password=password,account='Active')
    if c:
        time = datetime.now()
        date = datetime.now().date()
        request.session['empid'] = c[0].empCode
        request.session['fname'] = c[0].fname
        request.session['lname'] = c[0].lname
        request.session['managerId'] = c[0].managerId
        request.session['leave'] = c[0].leave
        employeeName = request.session['fname'] + request.session['lname']
        res = employeeDailyWork(employeeId=c[0].empCode, managerId=c[0].managerId,loginTime=time,date=date)
        res.save()
        eid = employeeDailyWork.objects.latest('id')
        feid = eid.id
        request.session['workId'] = feid
        print(feid)

        c = Attendance.objects.filter(employeeId=request.session['empid'], date=date)
        if not c:
            attendance = Attendance(employeeId=request.session['empid'], loginTime=time, logoutTime=time, date=date,
                                    status='Present', employeeName=employeeName)
            attendance.save()
        else:
            print('OK')
        return HttpResponseRedirect(reverse("employeeDashboard"))
    else:
        msg = 'You Are Not Valid User'
        return render(request, "employeeLogin.html", {'msg': msg})

# ----- Admin -----

def index(request):
    return render(request, "index.html")

def newAdmin(request):
    return render(request, "adminReg.html")

def saveAdmin(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['contact']
    gender = request.POST['gender']
    emailId = request.POST['email']
    password = request.POST['password']
    r = admin(fname=fname, lname=lname, contact=phone, gender=gender, emailId=emailId, password=password)
    r.save()
    if r:
        return HttpResponseRedirect(reverse("adminDashboard"))
    else:
        HttpResponseRedirect("Registration Failed")
    
def adminDetails(request):
    r = admin.objects.all()
    return render(request, "adminDashboard/adminDetails.html", {'r': r})


def adminReg(request):
    return render(request, 'EMSadmin/adminReg.html')
>>>>>>> db28b4f176e4b8006edd3ab34921a4e43be8bb43
