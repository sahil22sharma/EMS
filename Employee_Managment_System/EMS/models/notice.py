from datetime import datetime
from django.db import transaction

from django.db import models

class notice(models.Model):
    id = models.AutoField(primary_key=True)
    noticeDetails = models.CharField(max_length=100)
    noticeDate = models.DateField(default=datetime.now)