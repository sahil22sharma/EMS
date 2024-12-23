# models.py
from django.db import models
from django.contrib.auth.models import User
from .project import Project  # Assuming you have the Project model

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='task_as_employee')  # Assign task to an employee (User object)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)  # Assign task to a project
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Task status
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='task_as_manager')  # Manager creating the task
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    team_lead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='task_as_team_lead')  # Team lead for the task


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
