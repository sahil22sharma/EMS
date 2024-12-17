from datetime import datetime
from django.db import transaction

from django.db import models

# Manager model code:

class Manager(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    dob=models.DateField()
    address=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    bloodGroup=models.CharField(max_length=20)
    joinDate=models.DateField(null=True)
    salary = models.IntegerField(null=True, default=0)
    leave = models.IntegerField(null=True, default=0)
    qualification=models.CharField(max_length=30)
    activation_Date = models.DateTimeField(null=True)
    deactivation_Date = models.DateTimeField(null=True)
    account = models.CharField(max_length=20, default="Deactive")
    emailId=models.EmailField()
    password=models.CharField(max_length=20)
    about = models.CharField(max_length=40, null=True)
    managerCode = models.CharField(primary_key=True, editable=False, max_length=10, unique=True, default="None")
    image = models.ImageField(upload_to='images/', null=True)
    resume = models.FileField(upload_to='documents',null=True)

    def save(self, **kwargs):
        no = Manager.objects.count()  # Count method is used to count object form the Employee table
        if no == None:
            no = 1
        else:
            no = no + 1
        self.managerCode = "{}{:03}".format('MANAGER', no)
        super().save(*kwargs)
