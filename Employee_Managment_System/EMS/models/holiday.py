from django.db import models
from django.db import transaction
from datetime import datetime
from django.http import HttpResponseRedirect

class Holidays(models.Model):
    hoildayId = models.AutoField(primary_key=True)
    holidayName = models.CharField(max_length=20)
    hoildayDescription = models.CharField(max_length=30)
    hoildayDate = models.DateField()
    hoildayDay = models.CharField(max_length=20)

def saveHoliday(request):
    holidayId = models.AutoField(primary_key=True)
    holidayName = request.POST['holidayName']
    holidayDate = request.POST['holidayDate']
    holidayDay = request.POST['holidayDay']
    holidayDescription = request.POST['holidayDescription']

    h = Holidays(holidayId=holidayId, holidayName=holidayName, holidayDate=holidayDate, holidayDay= holidayDay, holidayDescription=holidayDescription)
    h.save()
    return HttpResponseRedirect(redirect_to=("holidays"))