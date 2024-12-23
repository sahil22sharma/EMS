from django.db import models
from django.contrib.auth.models import User  # assuming the manager is a User object, adjust if needed

class Project(models.Model):
    client_name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # assuming manager is a user
    start_date = models.DateField()
    deadline_date = models.DateField()

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
