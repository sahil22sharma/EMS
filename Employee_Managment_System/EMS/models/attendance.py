from django.db import models
from django.db import transaction
from datetime import datetime
from django.http import HttpResponseRedirect

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    employeeId = models.CharField(max_length=20)
    employeeName = models.CharField(max_length=20, null=True)
    date = models.DateField()
    loginTime = models.DateTimeField()
    logoutTime = models.DateTimeField()
    status = models.CharField(max_length=20, default='Absent')
    absentStatus = models.CharField(max_length=20, null=True)