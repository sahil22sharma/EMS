from django.db import models
from django.db import transaction
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='present_user')
    # user = models.CharField()
    # id = models.AutoField(primary_key=True)
    date = models.DateField()
    loginTime = models.CharField()
    logoutTime = models.CharField()
    status = models.CharField(max_length=20, default='Absent')
    absentStatus = models.CharField(max_length=20, null=True)