from django import forms
from .models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = {"password"}
        labels = {"employeeid": "Enter Employee ID", "fullname": "Enter Full Name", "gender":"Select Gender", "email":"Enter Email ID", "contact":"Enter Contact No."}