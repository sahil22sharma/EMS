from django.db import models
from datetime import datetime
from django.http import HttpResponseRedirect

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    employeeId = models.CharField(max_length=20)
    employeeName = models.CharField(max_length=20,null=True)
    managerId = models.CharField(max_length=20)
    clientId = models.IntegerField(null=True)
    projectName = models.CharField(max_length=20,null=True)
    date = models.DateField()
    workDescription = models.CharField(max_length=40, null=True)
    fileUpload = models.FileField(upload_to='documents',null=True)