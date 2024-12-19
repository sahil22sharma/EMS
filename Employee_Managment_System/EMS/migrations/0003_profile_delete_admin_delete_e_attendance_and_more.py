# Generated by Django 5.1.4 on 2024-12-19 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0002_admin_e_attendance_e_holidays_e_leave_e_monthsalary_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee')], max_length=10)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='admin',
        ),
        migrations.DeleteModel(
            name='E_Attendance',
        ),
        migrations.DeleteModel(
            name='E_Holidays',
        ),
        migrations.DeleteModel(
            name='E_Leave',
        ),
        migrations.DeleteModel(
            name='E_monthSalary',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='employeeDailyWork',
        ),
        migrations.DeleteModel(
            name='M_Attendance',
        ),
        migrations.DeleteModel(
            name='M_Holidays',
        ),
        migrations.DeleteModel(
            name='M_Leave',
        ),
        migrations.DeleteModel(
            name='M_tasks',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]