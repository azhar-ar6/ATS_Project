"""
URL configuration for ATS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.company, name='company'),
    path("home", views.homefunction, name="home"),
    path("about", views.aboutfunction, name="about"),
    path("login", views.loginfunction, name="login"),

    path("adminhome", views.adminhome, name="adminhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("adminlogout", views.adminlogout, name="adminlogout"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("adminchangepwd", views.adminchangepwd, name="adminchangepwd"),
    path("adminupdatepwd", views.adminupdatepwd, name="adminupdatepwd"),

    path("admincompany", views.admincompany, name="admincompany"),
    path("viewcompany", views.viewcompany, name="viewcompany"),
    path("addcompany", views.addcompany, name="addcompany"),
    path("insertcompany", views.insertcompany, name="insertcompany"),
    path("deletecompany", views.deletecompany, name="deletecompany"),
    path("companydeletion/<int:cid>", views.companydeletion, name="companydeletion"),

    path("adminclient", views.adminclient, name="adminclient"),
    path("viewclient", views.viewclient, name="viewclient"),
    path("addclient", views.addclient, name="addclient"),
    path("insertclient", views.insertclient, name="insertclient"),
    path("deleteclient", views.deleteclient, name="deleteclient"),
    path("clientdeletion/<int:clid>", views.clientdeletion, name="clientdeletion"),

    path("adminemployee", views.adminemployee, name="adminemployee"),
    path("addemployee", views.addemployee, name="addemployee"),
    path("deleteemployee", views.deleteemployee, name="deleteemployee"),
    path("employeedeletion/<int:eid>", views.employeedeletion, name="employeedeletion"),
    path("viewemployee", views.viewemployee, name="viewemployee"),
    path("employeelogin", views.employeelogin, name="employeelogin"),

    path("employeecompanymapping", views.employeecompanymapping, name="employeecompanymapping"),

]
