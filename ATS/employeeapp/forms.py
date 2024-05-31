from django import forms
from .models import JobPosting

class JobForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = '__all__'
        exclude = ['company_name', 'employee_id']