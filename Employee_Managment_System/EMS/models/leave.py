from django.db import models
from datetime import datetime

class Leave(models.Model):
    leaveId = models.AutoField(primary_key=True)
    employeeId = models.CharField(max_length=20)
    employeeName = models.CharField(max_length=20, null=True)
    managerId = models.CharField(max_length=20, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    totalDays = models.IntegerField(default=0)
    employeeReason = models.CharField(max_length=40)
    managerReason = models.CharField(max_length=40)
    appliedDate = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=10)
    leaveType = models.CharField(max_length=20, null=True)