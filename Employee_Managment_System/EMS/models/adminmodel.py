from datetime import datetime
from django.db import transaction

from django.db import models

# Admin model code:

class admin(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    emailId = models.EmailField()
    password = models.CharField(max_length=20)
