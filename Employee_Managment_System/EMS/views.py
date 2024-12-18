from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.core.mail import EmailMessage
from itertools import count

from django.db.models import Q, Sum
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse

from EMS.models.managermodel import Manager


def homepage(request):
    return render(request,'index.html')

def htmlpage(request):
    return render(request, 'index.html')
# def hello_world(request):
    #return HttpResponse("Hello, world!")

# ----- Manager -----

def managerRegistration(request):
    return render(request, "manager/managerReg.html")

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

    e = Manager(fname=fname, lname=lname, phone=phone, gender=gender,bloodGroup=bloodGroup,
                 dob=dob, address=address, state=state,  qualification=qualification,
                 emailId=emailId, password=password, image=image, resume=resume)
    e.save()
    if e:
        msg = "Your Application has been Submited. We will Back to you Soon"
        return render(request, "managerReg.html", {'msg': msg})
    else:
        return HttpResponse("error")

def managerLogin(request):
    return render(request, "/managerLogin.html")

def loginManager(request):
    emailId = request.POST['email']
    password = request.POST['password']
    c = Manager.objects.filter(emailId=emailId, password=password,account='Active')
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

from EMS.models.employeemodel import Employee, employeeDailyWork, E_Attendance, E_Holidays, E_Leave

def employeeRegistration(request):
    return render(request, "employee/employeeReg.html")

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
        return render(request, "employeeReg.html", {'msg': msg})
    else:
        return HttpResponse("error")

def employeeLogin(request):
    return render(request, "employee/employeeReg.html")

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

        c = E_Attendance.objects.filter(employeeId=request.session['empid'], date=date)
        if not c:
            attendance = E_Attendance(employeeId=request.session['empid'], loginTime=time, logoutTime=time, date=date,
                                    status='Present', employeeName=employeeName)
            attendance.save()
        else:
            print('OK')
        return HttpResponseRedirect(reverse("employeeDashboard"))
    else:
        msg = 'You Are Not Valid User'
        return render(request, "employeeLogin.html", {'msg': msg})

# ----- Admin -----
from EMS.models.adminmodel import admin

def index(request):
    return render(request, "index.html")

def newAdmin(request):
    return render(request, "EMSadmin/adminReg.html")

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
        return HttpResponseRedirect(reverse("home"))
    else:
        HttpResponseRedirect("Registration Failed")
    
def adminDetails(request):
    r = admin.objects.all()
    return render(request, "adminDashboard/adminDetails.html", {'r': r})

def adminReg(request):
    return render(request, 'EMSadmin/adminReg.html')

def adminlogin(request):
    return render(request, 'EMSadmin/adminLogin.html')

def loginAdmin(request):
    # print(request)
    emailId = request.POST.get('email')
    password = request.POST.get('password')
    c = admin.objects.filter(emailId=emailId, password=password)
    if c:
        return HttpResponseRedirect(reverse("home"))
       # return render(request, 'adminDashboard/index.html')
    else:
        msg = 'You Are Not The Valid User'
        print(msg)
        return render(request, "EMSadmin/adminLogin.html", {'msg': msg})
    



def login(request):
    if request.method == 'POST':
        # Get email and password from POST data
        email = request.POST.get('email')  # Form field 'email'
        password = request.POST.get('password')  # Form field 'password'
        
        # Verify user credentials
        c = admin.objects.filter(emailId=email, password=password)  # Adjust to your admin model
        if c.exists():  # Check if there's a matching admin
            return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
        else:
            # Invalid login credentials, show error message
            msg = 'You are not a valid user'
            print(msg)
            return render(request, "EMSadmin/adminLogin.html", {'msg': msg})  # Render the login page with error message
    else:
        # For GET request, simply render the login page
        print('NOTTTT')
        # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
        return render(request, "employee/employeeReg.html")




def adminIndexPage(request):
    employee = Employee.objects.filter(account='Active').count()
    manager = Manager.objects.filter(account='Active').count()
    # clientTotal = client.objects.filter(account='Active').count()
    # projectTotal = clientProject.objects.all().count()
    # p = clientProject.objects.filter(status='Working')
    # l = list(p)
    # for i in l:
    #     #m = get_object_or_404(Manager, managerCode=i.managerId)
    #     m = Manager.objects.filter(managerCode=i.managerId)
    #     print(m)
    # param = {'m': m, 'p': p, 'employee': employee, 'manager': manager, 'clientTotal': clientTotal,'projectTotal': projectTotal}
    # param = {'employee': employee, 'manager': manager, }
    return render(request, "EMSadmin/indexDash.html")

def base(request):
    return render(request, "EMSadmin/base.html")

""" def projectProgressAdmin(request,pk):
    pj = get_object_or_404(clientProject, pk=pk)
    pid =pj.projectId
    m = pj.managerId
    mng = Manager.objects.filter(managerCode=m)
    emp = Employee.objects.filter(managerId=m)

    p = employeeDailyWork.objects.filter(projectId=pid).order_by('-id')

    param = {'emp': emp, 'mng': mng, 'pj': pj, 'p': p}
    return render(request, "adminDashboard/projectProgress.html", param)"""

def employeeRequest(request):
    e1 = Employee.objects.filter(account='Deactive')
    return render(request, "adminDashboard/employeeRequest.html", {'e1': e1})

def managerRequest(request):
    # e1 = Manager.objects.filter(account='Deactive')
    return render(request, "EMSadmin/managerlist.html")





def testlogin(request):
    if request.method == 'POST':
        emailId = request.POST['email']
        password = request.POST['password']
        print(emailId,password)
        c = admin.objects.filter(emailId=emailId, password=password)  # Adjust to your admin model
        if c:
            # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
            # return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
            return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
        else:
            return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
    else:
        return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
        # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
