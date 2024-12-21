from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    manager = models.ForeignKey(User, related_name='managed_employees', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    aadhar_card = models.FileField(upload_to='aadhar_cards/', blank=True, null=True)
    cv = models.FileField(upload_to='cv_files/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'

