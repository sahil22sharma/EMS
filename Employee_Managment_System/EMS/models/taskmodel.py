from django.contrib.auth.models import User
from django.db import models
from models.projectmodel import Project


class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('blocked', 'Blocked'),
    ]

    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    tl=models.ForeignKey(User, related_name='t1_employee', on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey(User, related_name='managed_employees', on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3)
    start_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completion_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments = models.TextField(blank=True)
    # attachments = models.FileField(upload_to='tasks/', null=True, blank=True)
    # is_recurring = models.BooleanField(default=False)
    # estimated_time = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # time_spent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title