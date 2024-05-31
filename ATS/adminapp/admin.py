from django.contrib import admin
from .models import Admin,Company,Employee, EmployeeCompanyMapping
# Register your models here.

admin.site.register(Admin)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(EmployeeCompanyMapping)
