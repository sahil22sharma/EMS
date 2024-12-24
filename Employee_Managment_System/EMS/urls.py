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
    path('home/project/create',views.projectcreate,name='projectcreate'),
    path('delete_man/<int:user_id>/', views.delete_man, name='delete_man'),


    #Manager Routes
    path('register_man/',views.register_man,name='register_man'),
    path('man_login/',views.man_login,name='man_login'),
    path('man/task/create',views.taskcreate,name='taskcreate'),



    #Employee Routes
    path('register_emp/', views.register_emp, name='register_emp'),
    path('emp_login/',views.emp_login,name='emp_login'),
    path('home/task/status',views.taskstatus,name='taskstatus'),

    #Common Routes
    path('home/',views.home,name='home'),
    path('logout/',views.all_logout,name='logout'),
    path('home/attendance',views.all_attendance,name='all_attendance'),
    path('home/project/list',views.projectlist,name='projectlist'),
    path('home/task/list',views.tasklist,name='tasklist'),
    path('home/leave/list',views.leavelist,name='leavelist'),
    # path('home/notices'),

    # #Admin+Manager
    path('home/employee/list',views.employeelist,name='employeelist'),
    path('home/employee/request',views.employeerequest,name='employeerequest'),
    path('assign_manager_and_activate/', views.assign_manager_and_activate, name='assign_manager_and_activate'),
    path('delete_emp/<int:user_id>/', views.delete_emp, name='delete_emp'),
    
    #Manager + Employee
    path('home/leave/create',views.leavecreate,name='leavecreate')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)