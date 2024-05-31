from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from adminapp.models import Employee, EmployeeCompanyMapping, Company, Client

from .forms import JobForm
from .models import JobPosting


# Create your views here.
def employeehome(request):
    euname = request.session["euname"]
    return render(request, "employeehome.html", {"euname":euname})

def employeecompany(request):
    eid = request.session["eid"]
    print(eid)
    #company = Company.objects.all()
    #count = Company.objects.count()

    mappedcompany = EmployeeCompanyMapping.objects.all()
    ecompany = []
    print(mappedcompany)
    for company in mappedcompany:
        #print(company.employee.employeeid)
        #print(type(company.employee.employeeid))
        if(company.employee.employeeid == int(eid)):
            ecompany.append(company)

    print(ecompany)
    dir(ecompany)
    count = len(ecompany)
    return render(request, "employeecompany.html", {"eid": eid, "company": company, "count": count})


def checkemployeelogin(request):
    try:
        eid = int(request.POST["eid"])
    except ValueError:
        msg = 'Invalid Employee ID'
        return render(request, 'employeelogin.html', {'message': msg})

    epwd = request.POST["password"]
    selected_company = request.session.get('selected_company')

    if not selected_company:
        # Handle the case where no company is selected
        msg = 'No company selected'
        return render(request, 'employeelogin.html', {'message': msg})

    try:
        # Check if the employee with the given ID and password exists
        # and is associated with the selected company
        employee = Employee.objects.get(
            Q(employeeid=eid, password=epwd) &
            Q(employeecompanymapping__company__companyname__iexact=selected_company)
        )
        request.session["euname"] = eid
        return render(request, "employeehome.html", {"euname": eid})

    except Employee.DoesNotExist:
        # Employee not found or not associated with the selected company
        msg = 'Invalid Employee ID, Password, or Company'
        return render(request, 'employeelogin.html', {'message': msg})



def jobposting(request):
    euname = request.session.get('euname')  # Use get to avoid KeyError
    form = JobForm()

    if request.method == "POST":
        form1 = JobForm(request.POST)

        if form1.is_valid():
            job_posting = form1.save(commit=False)

            # Retrieve the associated company name from the session or other storage
            company_name = request.session.get('selected_company')
            if not company_name:
                message = "Company name not found"
                return render(request, 'error_template.html', {'msg': message})

            # Check if a job with the same job ID already exists
            if JobPosting.objects.filter(job_id=job_posting.job_id, company_name=company_name).exists():
                message = "Job with the same Job ID already exists."
                return render(request, "jobposting.html", {"msg": message, "form": form1, "euname": euname})

            # Associate the job posting with the company name and logged-in employee
            job_posting.company_name = company_name
            job_posting.employee_id = euname  # Adjust this based on your actual logic

            job_posting.save()

            message = "Job Posting Added Successfully"
            return render(request, "jobposting.html", {"msg": message, "form": form, "euname": euname})
        else:
            message = "Failed to Add Employee"
            return render(request, "jobposting.html", {"msg": message, "form": form1, "euname": euname})

    return render(request, "jobposting.html", {"form": form, "euname": euname})




def viewclient1(request):
    euname = request.session["euname"]
    client = Client.objects.all()
    count = Client.objects.count()
    return render(request, "viewclient1.html", {"clientdata": client, "count": count, "euname":euname})


def viewjobposting(request):
    euname = request.session.get("euname")
    company_name = request.session.get("selected_company")

    # Check if both employee ID and company name are available in the session
    if not euname or not company_name:
        message = "Employee ID or Company name not found in the session."
        return render(request, "error_template.html", {"msg": message})

    # Filter job postings for the specific employee and company
    jobpostings = JobPosting.objects.filter(employee_id=euname, company_name=company_name)
    count = jobpostings.count()

    return render(request,"viewjobposting.html", {"jobpostingdata": jobpostings, "count": count, "euname": euname})


def deletejobposting(request):
    euname = request.session.get("euname")
    company_name = request.session.get("selected_company")

    # Check if both employee ID and company name are available in the session
    if not euname or not company_name:
        message = "Employee ID or Company name not found in the session."
        return render(request, "error_template.html", {"msg": message})

    # Filter job postings for the specific employee and company
    jobpostings = JobPosting.objects.filter(employee_id=euname, company_name=company_name)
    count = jobpostings.count()

    return render(request,"editjobposting.html", {"jobpostingdata": jobpostings, "count": count, "euname": euname})

def  jobpostingdeletion(request, jobid):
    JobPosting.objects.filter(job_id=jobid).delete()
    #return HttpResponse("Deleted")
    return redirect("editjobposting")

def jobpostingediting(request, job_id):
    if not job_id:
        # Handle the case when job_id is not provided
        # For example, you may want to redirect the user or show an error message
        return HttpResponse("Invalid job ID")

    jobposting = get_object_or_404(JobPosting, job_id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=jobposting)
        if form.is_valid():
            form.save()
            return redirect('viewjobposting')
    else:
        form = JobForm(instance=jobposting)

    return render(request, 'editjobpostingform.html', {'jobposting': jobposting, 'form': form})


def empchangepwd(request):
    euname = request.session["euname"]
    return render(request, "empchangepwd.html", {"euname": euname})

def empupdatepwd(request):
    euname = request.session["euname"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(euname, opwd, npwd)
    flag = Employee.objects.filter(Q(employeeid=euname)&Q(password=opwd))
    if flag:
        print("Old Pwd is correct")
        Employee.objects.filter(employeeid=euname).update(password=npwd)
        print("updated...")
        msg = "Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg = "Old Password is incorrect"

    return render(request,"empchangepwd.html", {"euname": euname, "message": msg})

def emplogout(request):
    return redirect("company")


