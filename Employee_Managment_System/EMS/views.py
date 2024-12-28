from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models
from .models.profile import Profile
from .models.project import Project
from .models.task import Task
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponseBadRequest, HttpResponse
from .models.leave import Leave
from openpyxl import Workbook #type:ignore
from .models.attendance import Attendance


# Registration view
# def register_emp(request):
#     if request.method == 'POST':
#         role = 'employee' 
#         # Additional fields for the Manager model
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         phone = request.POST.get('contact')
#         email = request.POST.get('email')
#         username = email
#         gender = request.POST.get('gender')
#         dob = request.POST.get('dob')
#         address = request.POST.get('address')
#         state = request.POST.get('state')
#         qualification = request.POST.get('qualification')
#         password = request.POST.get('password')
#         image = request.FILES.get('image')  # Handling file uploads
#         aadhar_card = request.FILES.get('aadhar_card', None)
#         cv = request.FILES.get('cv', None)
#         # resume = request.FILES.get('resume')  # Handling file uploads
#         # Create the user
#         try:
#             # Create the user
#             user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password, is_active=False)
#             user.save()

#             # Create the Profile model with additional fields
#             profile = Profile.objects.create(user=user, role=role, fname=fname, lname=lname, phone=phone, gender=gender, dob=dob, address=address, state=state, qualification=qualification, image=image, aadhar_card=aadhar_card, cv=cv)
#             profile.save()

#             # If profile creation is successful, show a success message
#             messages.success(request, "Registration successful! Your account is awaiting approval.")
#             return render(request, 'employee/employeeLogin.html')

#         except Exception as e:
#             # If any error occurs, show an error message
#             messages.error(request, f"Registration failed. Please try again. Error: {str(e)}")
#     return render(request, 'employee/employeeReg.html') 


def register_emp(request):
    if request.method == 'POST':
        role = 'employee'

        # Getting the form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        username = email
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        state = request.POST.get('state')
        qualification = request.POST.get('qualification')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        aadhar_card = request.FILES.get('aadhar_card', None)
        cv = request.FILES.get('cv', None)

        # Check if the email already exists (to prevent duplicate registrations)
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'employee/employeeReg.html')  # Return to registration form

        try:
            # Creating the user
            user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password, is_active=False)
            user.save()

            # Creating the Profile model
            profile = Profile.objects.create(user=user, role=role, fname=fname, lname=lname, phone=phone, gender=gender, dob=dob, address=address, state=state, qualification=qualification, image=image, aadhar_card=aadhar_card, cv=cv)
            profile.save()

            # Success message
            messages.success(request, "Registration successful! Your account is awaiting approval.")
            return redirect('emp_login')   # Redirect to login page after registration

        except Exception as e:
            # If something goes wrong, show an error message
            messages.error(request, f"Registration failed. Please try again. Error: {str(e)}")
            return render(request, 'employee/employeeReg.html')  # Return to registration form if an error occurs

    return render(request, 'employee/employeeReg.html')
    

# Login view
def emp_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username , password)
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active: 
                print('y')
                login(request, user)
                today = datetime.today().date()

            # Check if the user has any attendance record for today
                attendance = Attendance.objects.filter(user=user, date=today).first()

                if not attendance:
                    # If no record exists for today, create a new one
                    Attendance.objects.create(
                        user=user,
                        date=today,
                        loginTime=datetime.now().strftime('%H:%M:%S'),
                        status='Present'
                    )
                else:
                    # If attendance exists, check if logout time is missing
                    if not attendance.logoutTime:
                        attendance.logoutTime = datetime.now().strftime('%H:%M:%S')  # Set logout time
                        attendance.status = 'Present'
                        attendance.save()
                
                return redirect('home') 
            else:
                print('User is inactive')
                messages.error(request, 'Your account is inactive. Please contact support.')
            # return redirect('home')  # Redirect to home page or desired page

        else:
            print('User is inactive')
            messages.error(request, 'Invalid username or password.')
    return render(request, 'employee/employeeLogin.html')

# Example home view (to be redirected after login/registration)



def register_admin(request):
    if request.method == 'POST':
        role = 'admin' 
        # Additional fields for the Manager model
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        username = email
        gender = request.POST.get('gender')
        # dob = request.POST.get('dob')
        # address = request.POST.get('address')
        # state = request.POST.get('state')
        # qualification = request.POST.get('qualification')
        password = request.POST.get('password')
        # image = request.FILES.get('image')  # Handling file uploads
        # resume = request.FILES.get('resume')  # Handling file uploads
        # Create the user
        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
        user.save()

        # Create the Profile model with additional fields
        profile = Profile.objects.create(user=user, role=role,fname=fname,lname=lname,phone=phone,gender=gender)
        r = profile.save()
        if r:
            return render(request, 'EMSadmin/adminLogin.html') 
    return render(request, 'EMSadmin/adminReg.html')    
    

# Login view
def admin_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username , password)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('y')
            login(request, user)
            # return redirect('home')  # Redirect to home page or desired page
            today = datetime.today().date()

            # Check if the user has any attendance record for today
            attendance = Attendance.objects.filter(user=user, date=today).first()

            if not attendance:
                # If no record exists for today, create a new one
                Attendance.objects.create(
                    user=user,
                    date=today,
                    loginTime=datetime.now().strftime('%H:%M:%S'),
                    status='Present'
                )
            else:
                # If attendance exists, check if logout time is missing
                if not attendance.logoutTime:
                    attendance.logoutTime = datetime.now().strftime('%H:%M:%S')  # Set logout time
                    attendance.status = 'Present'
                    attendance.save()
            

            return redirect('home') 

        else:
            print('N')
            messages.error(request, 'Invalid username or password.')
    return render(request, 'EMSadmin/adminLogin.html')



def register_man(request):
    if request.method == 'POST':
        role = 'manager' 
        # Additional fields for the Manager model
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        username = email
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        state = request.POST.get('state')
        qualification = request.POST.get('qualification')
        password = request.POST.get('password')
        image = request.FILES.get('image')  # Handling file uploads
        aadhar_card = request.FILES.get('aadhar_card', None)
        # resume = request.FILES.get('resume')  # Handling file uploads
        # Create the user
        if image:
            image.name = f"{fname}_{lname}_profile{image.name[image.name.rfind('.'):]}"

        if aadhar_card:
            aadhar_card.name = f"{fname}_{lname}_aadhar_card{aadhar_card.name[aadhar_card.name.rfind('.'):]}"

        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password,is_active = False)
        user.save()
        # Create the Profile model with additional fields
        profile = Profile.objects.create(user=user, role=role,fname=fname,lname=lname,phone=phone,gender=gender,dob=dob,address=address,state=state,qualification=qualification,image=image,aadhar_card=aadhar_card)
        r = profile.save()
        if r:
            return render(request, 'manager/managerLogin.html') 
    return render(request, 'manager/managerReg.html')    
   
# Login view
def man_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username , password)
        # Authenticate the user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        if user.is_active: 
            print('y')
            login(request, user)
            return redirect('home') 
        else:
            print('User is inactive')
            messages.error(request, 'Your account is inactive. Please contact support.')
            # return redirect('home')  # Redirect to home page or desired page
    else:
        print('User is inactive')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'manager/managerLogin.html')



def index(request):
    return render(request, 'index.html')
    
def home(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        
        # Fetch the count of employees and managers
        e1 = User.objects.filter(profile__role='employee')  
        employee_count = e1.count()
        e1 = User.objects.filter(profile__role='manager')  
        manager_count = e1.count()
        
        if role == 'admin':
            return render(request, 'EMSadmin/indexDash.html', {'employee_count': employee_count, 'manager_count': manager_count})
        
        elif role == 'manager':
            em = User.objects.filter(profile__manager=request.user).count()
            pro = Project.objects.filter(manager=request.user).count()
            return render(request, 'manager/managerDash.html', {'em': em, 'pro': pro})
        
        elif role == 'employee':
            # Get today's date
            today = timezone.now().date()
            
            # Filter attendance for today's loginTime
            att = Attendance.objects.filter(user=request.user, date=today).values('loginTime')
            
            # Print the attendance for debugging
            print("Today's Attendance:", att)
            
            # Pass attendance to the template
            return render(request, 'employee/employeeDash.html', {'att': att})

    return render(request, 'index.html')


def employeerequest(request):
    return render(request, "EMSadmin/employeeRequest.html")

def employeeStatus(request):
    return render(request, "EMSadmin/employeeStatus.html")
    
def baseEmployee(request):
    return render(request, "employee/base.html")

def employeeIndexPage(request):
    return render(request,"employee/employeeDash.html")

def baseManager(request):
    return render(request, "manager/base.html")

def managerIndexPage(request):
    return render(request,"manager/managerDash.html")

def managerEmployeelist(request):
    return render(request, "manager/employeeList.html")

def managerEmployeerequest(request):
    return render(request, "manager/employeeRequest.html")


def employeelist(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role=='admin':
            e1 = User.objects.filter(profile__role='employee',is_active=True)  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request,'EMSadmin/employeeList.html',{'e1':e1})
        elif role=='manager':
            e1 = User.objects.filter(profile__role='employee',is_active = True,profile__manager = request.user)  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request,'manager/employeeList.html',{'e1':e1})
    else:
        return render(request,'index.html')

# def employeerequest(request):
#     if request.user.is_authenticated:
#         role = request.user.profile.role
#         if role=='admin':
#             e1 = User.objects.filter(profile__role='employee',is_active=False)  # Fetch all User records
#             e1 = e1.select_related('profile')
#             return render(request,'EMSadmin/employeeRequest.html',{'e1':e1})
#         elif role=='manager':
#             e1 = User.objects.filter(profile__role='employee')  # Fetch all User records
#             e1 = e1.select_related('profile')
#             return render(request,'EMSadmin/employeeRequest.html',{'e1':e1})
#     else:
#         return render(request,'index.html')
    
def employeerequest(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role == 'admin':
            e1 = User.objects.filter(profile__role='employee', is_active=False)  # Fetch all User records
            e1 = e1.select_related('profile')
            managers = User.objects.filter(profile__role='manager')  # Get managers for assignment
            return render(request, 'EMSadmin/employeeRequest.html', {'e1': e1, 'managers': managers})
        elif role == 'manager':
            e1 = User.objects.filter(profile__role='employee')  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request, 'manager/employeeRequest.html', {'e1': e1})
    else:
        return render(request, 'index.html')





def managerlist(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role=='admin':
            e1 = User.objects.filter(profile__role='manager',is_active=True)  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request,'EMSadmin/managerlist.html',{'e1':e1})
    else:
        return render(request,'index.html')
    
    
def managerrequest(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role=='admin':
            e1 = User.objects.filter(profile__role='manager',is_active=False)  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request,'EMSadmin/managerRequest.html',{'e1':e1})
    else:
        return render(request,'index.html')

def all_logout(request):
    # Log out the user
    now = datetime.now()
        
        # Print the date and time separately
    print("Date:", now.date())  # Prints only the date (YYYY-MM-DD)
    print("Time:", now.strftime("%H:%M:%S"))  # Prints only the time (HH:MM:SS)

        # Update the user's attendance record with the logout time
    today = now.date()  # Current date
    try:
            # Fetch the attendance record for today
        attendance = Attendance.objects.get(user=request.user, date=today)
            
        # Set the logout time
        attendance.logoutTime = now.strftime("%H:%M:%S")
        attendance.save()  # Save the logout time in the record
            
        print(f"Logout time for {request.user.username}: {attendance.logoutTime}")
    except Attendance.DoesNotExist:
            # If there's no attendance record for today, you could log this, but no need to create one
        print("No attendance record found for today.")
    logout(request)
    
    # Redirect to the login page or a different page after logout
    return render(request,'index.html')  # Replace with your login page name or URL

    
# def all_attendance(request):
#     if request.user.is_authenticated:
#         role = request.user.profile.role  # Assuming there's a role field in User profile
        
#         if role == 'admin' or role == 'manager':  # Only allow admin/manager to view all attendance data
#             attendance_data = Attendance.objects.all()  # Fetch all attendance records
            
#             # Print attendance data for debugging
#             for attendance in attendance_data:
#                 print(f"User: {attendance.user.get_full_name()}, Date: {attendance.date}, Login Time: {attendance.loginTime}, Logout Time: {attendance.logoutTime}, Status: {attendance.status}")
            
#             return render(request, 'EMSadmin/attendance.html', {'e1': attendance_data})
        
#         elif role == 'manager':
#             attendance_data = Attendance.objects.filter(user = request.user)
#             return render(request, 'manager/attendance.html', {'e1': attendance_data})
        
#         elif role == 'employee':
#             attendance_data = Attendance.objects.filter(user = request.user)
#             return render(request, 'employee/attendance.html', {'e1': attendance_data})
        
#         else:
#             return render(request, 'index.html')  # If the user doesn't have proper permissions
    
#     else:
#         return render(request, 'index.html')  #

def all_attendance(request):
    if request.user.is_authenticated:
        role = request.user.profile.role  # Assuming there's a role field in User profile
        
        # Get the date from the GET request, default to today's date if no date is selected
        filter_date = request.GET.get('date', datetime.today().date())  # Default to today if no date is passed
        
        # Get the month from the GET request if provided, otherwise use the current month
        filter_month = request.GET.get('month', datetime.today().month)  # Default to current month
        
        # Fetch attendance data based on user role and date/month filter
        if role == 'admin' or role == 'manager':  # Only allow admin/manager to view all attendance data
            if isinstance(filter_date, str) and filter_date != '':  # Check if date is provided as a string
                # Filter attendance by exact date if a specific date is passed
                attendance_data = Attendance.objects.filter(date=filter_date)
            else:
                # Filter attendance by month if no specific date is passed
                attendance_data = Attendance.objects.filter(date__month=filter_month)
        elif role == 'manager':
            attendance_data = Attendance.objects.filter(user=request.user, date__month=filter_month)  # Filter by user and month
        elif role == 'employee':
            attendance_data = Attendance.objects.filter(user=request.user, date__month=filter_month)  # Filter by user and month
        else:
            return render(request, 'index.html')  # If the user doesn't have proper permissions

        # Export functionality
        if 'export' in request.GET:
            # Create an Excel workbook and sheet
            wb = Workbook()
            ws = wb.active
            ws.title = 'Attendance Records'
            
            # Add headers to the Excel file
            headers = ['Name', 'Date', 'Login Time', 'Logout Time', 'Status']
            ws.append(headers)
            
            # Add attendance data to the Excel file
            for attendance in attendance_data:
                ws.append([
                    attendance.user.get_full_name(),
                    attendance.date,
                    attendance.loginTime,
                    attendance.logoutTime,
                    attendance.status
                ])
            
            # Create a response to send the Excel file to the user
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="attendance_records_{filter_month}.xlsx"'
            wb.save(response)
            return response
        
        # Render the attendance page with the filtered data and the filter date
        return render(request, 'EMSadmin/attendance.html', {'e1': attendance_data, 'filter_date': filter_date, 'filter_month': filter_month})

    else:
        return render(request, 'index.html')
    


def assign_manager_and_activate(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        manager_id = request.POST.get('manager')
        activate_account = request.POST.get('activate_account') == 'True'  # Convert the checkbox value to boolean

        # Debugging prints (optional, can be removed later)

        try:
            # Fetch employee and manager objects from the database
            employee = User.objects.get(id=employee_id)
            manager = User.objects.get(id=manager_id)

            # Assign the manager to the employee's profile
            employee.profile.manager = manager  # Assign the actual manager instance
            employee.profile.save()

            # Activate the employee account if the checkbox is checked
            if activate_account:
                employee.is_active = True  # Set the account to active
                employee.save()  # Save the changes to the User model

            # Show success message
            messages.success(request, f"Manager assigned and account activated for {employee.get_full_name()}.")

            # Redirect to the employee request page (or any other page you prefer)
            return redirect('employeelist')

        except User.DoesNotExist:
            # Handle the case where the employee or manager is not found
            messages.error(request, "User or Manager not found.")
            return redirect('employeerequest')


    else:
        return HttpResponseBadRequest("Invalid request method.")


def manageractivation(request):
    if request.method == "POST":
        manager_id = request.POST.get('employee_id')
        activate_account = request.POST.get('activate_account') == 'True'  # Convert the checkbox value to boolean

        # Debugging prints (optional, can be removed later)

        try:
            # Fetch employee and manager objects from the database
            manager = User.objects.get(id=manager_id)

            # Assign the manager to the employee's profile
            # Activate the employee account if the checkbox is checked
            if activate_account:
                manager.is_active = True  # Set the account to active
                manager.save()  # Save the changes to the User model

            # Show success message
            messages.success(request, f"Manager assigned and account activated for {manager.get_full_name()}.")

            # Redirect to the employee request page (or any other page you prefer)
            return redirect('managerlist')

        except User.DoesNotExist:
            # Handle the case where the employee or manager is not found
            messages.error(request, "User or Manager not found.")
            return redirect('managerrequest')


    else:
        return HttpResponseBadRequest("Invalid request method.")

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def delete_emp(request, user_id):
    """Handle the deletion of a user."""
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = get_object_or_404(User, id=user_id)
            user.delete()  # Delete the user
            messages.success(request, f'User {user.username} has been deleted successfully.')
        return redirect('employeelist')  # Redirect back to the employee list page (adjust if needed)
    

def delete_man(request, user_id):
    """Handle the deletion of a user."""
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = get_object_or_404(User, id=user_id)
            user.delete()  # Delete the user
            messages.success(request, f'User {user.username} has been deleted successfully.')
        return redirect('managerlist')  # Redirect back to the employee list page (adjust if needed)
    
def tasklist(request):
    # taskl = Task.objects.filter(manager=request.user)
    # return render(request, "manager/tasklist.html",{'taskl':taskl})
    if request.user.is_authenticated:
            role = request.user.profile.role
            if role == 'manager':
                taskl = Task.objects.filter(manager=request.user)
                return render(request, "manager/tasklist.html",{'taskl':taskl})
            elif role == 'employee':
                manager_profile = Profile.objects.get(user =request.user)
            # Get the list of employees who are assigned to this manager
                emplist = Profile.objects.filter(manager=manager_profile.user)
                taskl = Task.objects.filter(employee=request.user)
                print(manager_profile)
                print(emplist)
                return render(request,'employee/tasklist.html',{'taskl':taskl})

def taskcreate(request):
    if request.method == 'POST':
        # Handle form submission
        project_id = request.POST.get('project')
        employee_id = request.POST.get('employee')
        title = request.POST.get('task-title')
        description = request.POST.get('description')
        due_date = request.POST.get('date')
        manager = request.user
        project = Project.objects.get(id=project_id) if project_id else None
        
        if employee_id == 'all':
            emp = User.objects.filter(profile__manager = request.user)
            for i in emp:
                task = Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                employee=i,
                project=project,
                manager=manager
                )
                # task.save()
        else:
            employee = User.objects.get(id=employee_id) if employee_id else None
        # Handle creating the task
        # project = Project.objects.get(id=project_id) if project_id else None
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                employee=employee,
                project=project,
                manager=manager
            )
        print(project_id,employee_id,title,description)
        return redirect('tasklist')  # Redirect to the task list after creation

    projects = Project.objects.filter(manager=request.user)
    employees = User.objects.filter(profile__manager=request.user)

    return render(request, 'manager/taskcreate.html', {
        'projects': projects,
        'employees': employees
    })
    # return render(request, "manager/taskcreate.html")

def projectlist(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role == 'admin':
            list = Project.objects.all()
            return render(request,'EMSadmin/projectlist.html',{'list':list})
        elif role == 'manager':
            list = Project.objects.filter(manager=request.user)
            return render(request,'manager/projectlist.html',{'list':list})
        elif role == 'employee':
            list = Project.objects.filter(manager=request.user.profile.manager)
            return render(request,'employee/projectlist.html',{'list':list})
        

def projectcreate(request):
    if request.method == 'POST':
        # Retrieve form data from request.POST
        client_name = request.POST.get('client_name')
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        manager_id = request.POST.get('manager')  # This is the manager selected from the dropdown
        start_date = request.POST.get('start_date')
        deadline_date = request.POST.get('deadline_date')

        # Handle the manager - it's a ForeignKey, so we get the User object
        manager = User.objects.get(id=manager_id) if manager_id else None

        # Create a new Project object and save it to the database
        project = Project(
            client_name=client_name,
            project_name=project_name,
            description=description,
            manager=manager,
            start_date=start_date,
            deadline_date=deadline_date
        )
        project.save()

        # Redirect to another page (e.g., project list or success page)
        return redirect('projectlist')  # Adjust to the appropriate URL name
    else:
        # GET request - render the form
        e1 = User.objects.filter(profile__role='manager',is_active=True)  # Fetch all User records
        managers = e1.select_related('profile') # Get all users for manager selection
        return render(request, 'EMSadmin/projectcreate.html',{'managers':managers})
    # return render(request,'EMSadmin/projectcreate.html')

def status(request):
    return render(request,'employee/taskstatus.html')


def taskstatus(request):
    if request.method == 'POST':
        # Get the task ID and the selected status from the form
        task_id = request.POST.get('employee_id')
        status = request.POST.get('status')
        # print(status)
        # Ensure task ID and status are provided
        if task_id and status:
            try:
                # Get the task from the database
                task = Task.objects.get(id=task_id)

                # Update the status of the task
                task.status = status

                if status == 'in_progress':
                # Set the start_at field to the current date
                    task.start_at = timezone.now().date()

                # Save the changes to the task
                task.save()

                # Optionally, you can add a message to indicate success
                messages.success(request, "Task status updated and start date set successfully.")

                # Redirect to the task list page (or wherever you want to redirect after saving)
                return redirect('tasklist')  # Assuming you have a URL pattern named 'task_list'

            except Task.DoesNotExist:
                # Handle the case where the task does not exist
                messages.error(request, "Task not found.")
                return redirect('tasklist')  # Or any other page
        else:
            # Handle the case where data is incomplete
            messages.error(request, "Please provide all the required fields.")
            return redirect('tasklist')  # Or any other page
    else:
        # If the request method is not POST, redirect to the task list page
        return redirect('tasklist')  # Or any other page



def leavelist(request):
    return render(request,'manager/leavelist.html')

# def leavecreate(request):
#     return render(request,'manager/leavecreate.html')

def leavecreate(request):
    if request.method == 'POST':
        # Get data from the form
        employee_id = request.user
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        total_days = request.POST.get('totalDays')
        employee_reason = request.POST.get('employeeReason')
        status = 'pending'
        leave_type = request.POST.get('leaveType')
        
        # Convert dates to proper format
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse("Invalid date format", status=400)
        
        # Calculate the total days if it's not provided (for validation)
        if not total_days:
            total_days = (end_date - start_date).days + 1  # +1 because the start day counts as a leave day
            
            # If the end date is before the start date
            if total_days < 0:
                return HttpResponse("End date must be later than start date.", status=400)
        
        # Create a new leave request
        leave_request = Leave.objects.create(
            employeeId=employee_id,
            startDate=start_date,
            endDate=end_date,
            totalDays=total_days,
            employeeReason=employee_reason,
            status=status,
            leaveType=leave_type,
        )
        
        # You can either redirect to a success page or render a success message
        return redirect('leavelist')  # Adjust this to your success URL
        
    # If GET request, render the form
    return render(request, 'manager/leavecreate.html')