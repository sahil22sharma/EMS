from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),

    # Signup Routes
    path('adminReg/',views.adminReg, name='adminReg'),
    path('employeeReg/',views.employeeRegistration, name='employeeReg'),
    path('managerReg/',views.managerRegistration, name='managerReg'),
    path('saveAdmin/',views.saveAdmin,name='saveAdmin'),
    path('adminlogin/',views.adminlogin,name='adminlogin'), # redirect to login page
    path('loginAdmin/',views.loginAdmin,name='loginAdmin'), 
    # path('login/',views.login,name='login'),
    path('login/', views.login, name='login'),  # The login page URL

    path('testlogin/',views.testlogin,name='testlogin')

]