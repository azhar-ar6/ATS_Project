from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Admin, Company, Employee, Client
from .forms import AddEmployeeForm

def homefunction(request):
    return render(request, "index.html")

def aboutfunction(request):
    return render(request, "about.html")

def companyfunction(request):
    return render(request, "companyname.html")

def loginfunction(request):
    return render(request, "login.html")


# Create your views here.
def adminhome(request):
    auname = request.session["auname"]
    return render(request, "adminhome.html", {"adminuname":auname})

def adminlogout(request):
    return render(request, "login.html")




def company(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name', '').strip().lower()
        if company_name:
            try:
                company = Company.objects.get(companyname__iexact=company_name)
                request.session['selected_company'] = company_name
                return render(request, 'employeelogin.html')  # Render the login page HTML
            except Company.DoesNotExist:
                messages.error(request, 'Company name does not exist. Please try again.')

    return render(request, 'companyname.html')


def checkadminlogin(request):
    adminuname = request.POST["username"]
    adminpwd = request.POST["password"]
    # data = adminuname + "," + adminpwd

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["auname"] = adminuname
        return render(request, "adminhome.html", {"adminuname":adminuname})

    else:
        msg = "Login Failed"
        return render(request, "login.html", {"message":msg})



def viewemployee(request):
    employee = Employee.objects.all()
    count = Employee.objects.count()
    return render(request, "viewemployee.html", {"employeedata": employee, "count": count})


def viewcompany(request):
    company = Company.objects.all()
    count = Company.objects.count()
    return render(request, "viewcompany.html", {"companydata": company, "count": count})

def viewclient(request):
    client = Client.objects.all()
    count = Client.objects.count()
    return render(request, "viewclient.html", {"clientdata": client, "count": count})


def adminemployee(request):
    auname = request.session["auname"]
    return render(request, "adminemployee.html", {"adminuname":auname})


def admincompany(request):
    auname = request.session["auname"]
    return render(request, "admincompany.html", {"adminuname":auname})

def adminclient(request):
    auname = request.session["auname"]
    return render(request, "adminclient.html", {"adminuname":auname})


def addcompany(request):
    auname = request.session["auname"]
    return render(request, "addcompany.html", {"adminuname":auname})

def addclient(request):
    auname = request.session["auname"]
    return render(request, "addclient.html", {"adminuname":auname})


def insertcompany(request):
    if request.method == "POST":
        company = request.POST["company"]

        company = Company(companyname=company)
        Company.save(company)

        message = "Company Added Successfully"

        return render(request, "addcompany.html", {"msg": message})

def insertclient(request):
    if request.method == "POST":
        client = request.POST["client"]

        client = Client(clientname=client)
        Client.save(client)

        message = "Client Added Successfully"

        return render(request, "addclient.html", {"msg": message})


def deletecompany(request):
    company = Company.objects.all()
    count = Company.objects.count()
    return render(request, "deletecompany.html", {"companydata": company, "count": count})

def deleteclient(request):
    client = Client.objects.all()
    count = Client.objects.count()
    return render(request, "deleteclient.html", {"clientdata": client, "count": count})


def companydeletion(request, cid):
    Company.objects.filter(id=cid).delete()
    return redirect("deletecompany")

def clientdeletion(request, clid):
    Client.objects.filter(id=clid).delete()
    return redirect("deleteclient")


def addemployee(request):
    form = AddEmployeeForm()
    if request.method == "POST":
        form1 = AddEmployeeForm(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Emplpoyee Added Successfully"
            return render(request, "addemployee.html", {"msg": message,"form": form})
        else:
            message = "Failed to Add Employee"
            return render(request, "addemployee.html", {"msg": message,"form": form})
    return render(request, "addemployee.html", {"form": form})

def deleteemployee(request):
    employee = Employee.objects.all()
    count = Employee.objects.count()
    return render(request, "deleteemployee.html", {"employeedata": employee, "count": count})

def  employeedeletion(request, eid):
    Employee.objects.filter(employeeid=eid).delete()
    #return HttpResponse("Deleted")
    return redirect("deleteemployee")

def employeecompanymapping(request):
    auname = request.session["auname"]
    return render(request, "employeecompanymapping.html", {"adminuname":auname})

def adminchangepwd(request):
    return render(request, "adminchangepwd.html")


def employeelogin(request):
    return render(request, "employeelogin.html")


def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request, "adminchangepwd.html", {"adminuname": auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(auname, opwd, npwd)
    flag = Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("Old Pwd is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated...")
        msg = "Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg = "Old Password is incorrect"

    return render(request,"adminchangepwd.html", {"adminuname": auname, "message": msg})
