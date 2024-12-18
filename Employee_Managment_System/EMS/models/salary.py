from django.db import models
from django.db import transaction
from datetime import datetime
from django.http import HttpResponseRedirect

class monthSalary(models.Model):
    id = models.AutoField(primary_key=True)
    empCode=models.CharField(max_length=20)
    dateCreated=models.DateTimeField(null=True)
    date = models.DateField(null=True)
    month = models.CharField(max_length=20,null=True)
    year = models.IntegerField(null=True)
    totalTime = models.IntegerField()
    perDaySalary=models.IntegerField()
    finalSalary = models.IntegerField()
    status = models.CharField(max_length=20,null=True)
    
class perDaySalary(models.Model):
    empCode=models.CharField(max_length=20)
    date=models.DateField()
    totalTime = models.IntegerField()
    daySalary = models.IntegerField()