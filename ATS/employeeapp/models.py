from django.db import models

# Create your models here.
from django.db import models
from adminapp.models import Client, Company, EmployeeCompanyMapping, Employee
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class JobPosting(models.Model):
    company_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    job_id = models.CharField(max_length=20, unique=True)
    date = models.DateField(auto_now_add=True)
    job_title = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    exp_min = models.CharField(max_length=2, blank=False)
    exp_max = models.CharField(max_length=2, blank=False)
    position_type = models.CharField(max_length=20, choices=[
        ('full_time', 'Full Time'),
        ('temporary', 'Temporary'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
    ])
    duration = models.CharField(max_length=20, blank=True, null=True)
    interview_mode = models.CharField(max_length=100, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    end_client = models.CharField(max_length=100)
    salary_offer = models.CharField(max_length=20)
    budget_from_client = models.CharField(max_length=20)
    job_description = models.TextField()





