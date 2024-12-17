from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),

    # Signup Routes
    path('adminReg/',views.adminReg, name='adminReg'),
    path('employeeReg/',views.employeeRegistration, name='employeeReg'),
    path('managerReg/',views.managerRegistration, name='managerReg'),
]