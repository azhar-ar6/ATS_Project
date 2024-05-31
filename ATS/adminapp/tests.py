from django.test import TestCase
from.models import Admin, Employee  # Replace with your actual model

class AdminModelTests(TestCase):
    def setUp(self):
        self.admin = Admin.objects.create(username="admin", password="admin")

    def test_admin_creation(self):
        self.assertTrue(Admin.objects.filter(username="admin").exists())

class EmployeeModelTests(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employeeid=5432, fullname="Mohammad Sahila Sana", gender="M", password="5432", email="sana@gmail.com", contact="9949675802")

    def test_employee_creation(self):
        self.assertTrue(Employee.objects.filter(employeeid=5432).exists())
