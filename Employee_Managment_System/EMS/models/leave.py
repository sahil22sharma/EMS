from django.db import models
from datetime import datetime

class Leave(models.Model):
    # Define choices for leave types
    LEAVE_STATUS_CHOICES = [
        ('casual_leave', 'Casual Leave'),
        ('paid_leave', 'Paid Leave'),
        ('sick_leave', 'Sick Leave'),
        ('maternity_leave', 'Maternity Leave'),
        ('paternity_leave', 'Paternity Leave'),
        ('unpaid_leave', 'Unpaid Leave'),
        ('other', 'Other'),
    ]
    
    employeeId = models.CharField(max_length=20)
    startDate = models.DateField()
    endDate = models.DateField()
    totalDays = models.IntegerField(default=0)
    employeeReason = models.CharField(max_length=40)
    appliedDate = models.DateTimeField(default=datetime.now, blank=True)
    
    # Use choices for status
    status = models.CharField(
        max_length=20,
        choices=LEAVE_STATUS_CHOICES,
        default='casual_leave',  # You can set a default if needed
    )
    
    leaveType = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"Leave Request {self.employeeId} - {self.get_status_display()}"
