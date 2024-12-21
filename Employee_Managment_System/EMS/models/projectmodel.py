from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    client=models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    manager = models.ForeignKey(User, related_name='managed_employees', on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    
