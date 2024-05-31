from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("checkemployeelogin", views.checkemployeelogin, name="checkemployeelogin"),
    path("employeehome", views.employeehome, name="employeehome"),
    path("jobposting", views.jobposting, name="jobposting"),
    path("viewclient1", views.viewclient1, name="viewclient1"),
    path("viewjobposting", views.viewjobposting, name="viewjobposting"),
    path("deletejobposting", views.deletejobposting, name="deletejobposting"),
    path("jobpostingdeletion/<str:job_id>", views.jobpostingdeletion, name="jobpostingdeletion"),
    path("jobpostingediting/<str:job_id>/", views.jobpostingediting, name="jobpostingediting"),
    path("empchangepwd", views.empchangepwd, name="empchangepwd"),
    path("empupdatepwd", views.empupdatepwd, name="empupdatepwd"),
    path("emplogout", views.emplogout, name="emplogout"),

]