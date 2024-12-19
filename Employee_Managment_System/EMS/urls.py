from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register_emp, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/',views.home,name='home'),
    # path('',views.homepage,name="home"),

    # # Signup Routes
    # path('adminReg/',views.adminReg, name='adminReg'),
    # path('adminlogin/',views.adminlogin, name='adminlogin'),
    # path('employeeReg/',views.employeeRegistration, name='employeeReg'),
    # path('employeeLogin/',views.employeeLogin, name='employeeLogin'),
    # path('managerReg/',views.managerRegistration, name='managerReg'),
    # path('managerLogin/',views.managerLogin, name='managerLogin'),
    # path('saveAdmin/',views.saveAdmin,name='saveAdmin'),
    # path('saveManager/',views.saveManager,name='saveManager'),
    # path('saveEmployee/',views.saveEmployee,name='saveEmployee'),
    # path('adminLogin/',views.adminlogin,name='adminlogin'), # redirect to login page
    # # path('loginAdmin/',views.loginAdmin,name='loginAdmin'), 
    # path('login/', views.login, name='login'),  # The login page URL

    # path('testlogin/',views.testlogin,name='testlogin'),
    # path('adminDash/',views.base),
    # path('adminDash/Index', views.adminIndexPage,name='adminDash'),
    # path('adminDash/manager', views.managerRequest,name='managerRequest'),
    # path('testlogin/',views.testlogin,name='testlogin'),
    # path('testloginEmployee/',views.testloginEmployee,name='testloginEmployee'),
    # path('testloginManager/',views.testloginManager,name='testloginManager'),
    # path('adminDash/managerlist', views.managerlist,name='managerlist'),
    # path('adminDash/managerrequest', views.managerrequest,name='managerrequest'),
    # path('adminDash/employeelist', views.employeelist,name='employeelist'),
    # path('adminDash/employeerequest', views.employeerequest,name='employeerequest'),
    path('testlogin/',views.testlogin,name='testlogin'),
    path('adminDash/',views.base),
    path('adminDash/Index', views.adminIndexPage,name='adminDash'),
    path('adminDash/manager', views.managerRequest,name='managerRequest'),
    path('testlogin/',views.testlogin,name='testlogin'),
    path('testloginEmployee/',views.testloginEmployee,name='testloginEmployee'),
    path('testloginManager/',views.testloginManager,name='testloginManager'),
    path('adminDash/managerlist', views.managerlist,name='managerlist'),
    path('adminDash/managerrequest', views.managerrequest,name='managerrequest'),
    path('adminDash/employeelist', views.employeelist,name='employeelist'),
    path('adminDash/employeerequest', views.employeerequest,name='employeerequest'),
    path('adminDash/employeeStatus',views.employeeStatus,name='employeestatus'),

    path('employeeDash/',views.baseEmployee),
    path('employeeDash/Index', views.employeeIndexPage,name='employeeDash'),
    path('managerDash/',views.baseManager),
    path('managerDash/Index', views.managerIndexPage,name='managerDash'),
    path('managerDash/employeelist', views.managerEmployeelist,name='managerEmployeelist'),
    path('managerDash/employeerequest', views.managerEmployeerequest,name='managerEmployeerequest'),
]