from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index),
    #Admin Routes
    path('register_admin/',views.register_admin,name='register_admin'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('home/manager/list',views.managerlist,name='managerlist'),
    path('home/manager/request',views.managerrequest,name='managerrequest'),
    path('manageractivation/',views.manageractivation,name='manageractivation'),
    path('delete_man/<int:user_id>/', views.delete_man, name='delete_man'),


    #Manager Routes
    path('register_man/',views.register_man,name='register_man'),
    path('man_login/',views.man_login,name='man_login'),
    path('man/task/list',views.tasklist,name='tasklist'),
    path('man/task/create',views.taskcreate,name='taskcreate'),



    #Employee Routes
    path('register_emp/', views.register_emp, name='register_emp'),
    path('emp_login/',views.emp_login,name='emp_login'),


    #Common Routes
    path('home/',views.home,name='home'),
    path('logout/',views.all_logout,name='logout'),
    path('home/attendance',views.all_attendance,name='all_attendance'),
    # path('home/task'),
    path('home/project/list',views.projectlist,name='projectlist'),
    path('home/project/create',views.projectcreate,name='projectcreate'),
    # path('home/leave'),
    # path('home/notices'),

    # #Admin+Manager
    path('home/employee/list',views.employeelist,name='employeelist'),
    path('home/employee/request',views.employeerequest,name='employeerequest'),
    path('assign_manager_and_activate/', views.assign_manager_and_activate, name='assign_manager_and_activate'),
    path('delete_emp/<int:user_id>/', views.delete_emp, name='delete_emp'),
    

    # path('',views.homepage,name="home"),

    # # Signup Routes
 
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
    # path('testlogin/',views.testlogin,name='testlogin'),
    # path('adminDash/',views.base),
    # path('adminDash/Index', views.adminIndexPage,name='adminDash'),
    # path('adminDash/manager', views.managerRequest,name='managerRequest'),
    # path('testlogin/',views.testlogin,name='testlogin'),
    # path('testloginEmployee/',views.testloginEmployee,name='testloginEmployee'),
    # path('testloginManager/',views.testloginManager,name='testloginManager'),
    # path('adminDash/managerlist', views.managerpage,name='managerlist'),
    # path('adminDash/managerrequest', views.managerrequest,name='managerrequest'),
    # path('adminDash/employeelist', views.allEmployee,name='employeelist'),
    # path('adminDash/employeerequest', views.employeerequest,name='employeerequest'),
    # path('adminDash/employeeStatus',views.employeestatus,name='employeestatus'),

    # path('employeeDash/',views.baseEmployee),
    # path('employeeDash/Index', views.employeeIndexPage,name='employeeDash'),
    # path('managerDash/',views.baseManager),
    # path('managerDash/Index', views.managerIndexPage,name='managerDash'),
    # path('managerDash/employeelist', views.managerEmployeelist,name='managerEmployeelist'),
    # path('managerDash/employeerequest', views.managerEmployeerequest,name='managerEmployeerequest'),
    # path('allEmployee/',views.allEmployee,)
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)