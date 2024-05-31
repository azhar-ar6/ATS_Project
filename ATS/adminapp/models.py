from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)


    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=100, blank=False, unique=True)


    class Meta:
        db_table = "company_table"

    def __str__(self):
        return self.companyname

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employeeid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("F", "Female"), ("M", "Male"), ("O", "Other"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)
    #department = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=100, blank=False, default="ATS")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "employee_table"

    def __str__(self):
        return str(self.employeeid)


class EmployeeCompanyMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = "employeecompanymapping_table"

    def __str__(self):
        return f"{self.company.companyname}-{self.employee.employeeid}-{self.employee.fullname}"


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=100, blank=False, unique=True)

    class Meta:
        db_table = "client_table"

    def __str__(self):
        return self.clientname


