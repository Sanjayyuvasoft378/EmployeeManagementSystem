from django.shortcuts import render,redirect
from django.http import HttpResponse
from Emp_app.models import *
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")

def add_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        mobileNo = request.POST['mobileNo']
        salary = int(request.POST['salary'])
        role = request.POST['role']
        department = request.POST['department']
        bonus = int(request.POST['bonus'])
        hireDate = request.POST['hireDate']
        New_Emp = Employee(name=name,mobileNo=mobileNo,salary=salary,role_id=role,department_id=department,bonus=bonus,hireDate=datetime.now())
        New_Emp.save()
        # return HttpResponse("employee added successfully")
        return redirect("/emp_app/view_emp")
    elif request.method == "GET":
        return render(request,"add_emp.html")
    else:
        return HttpResponse("An Exception Occured   ")

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps":emps
    }
    return render(request,"view_emp.html",context)

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            data = Employee.objects.get(id=emp_id)
            data.delete()
            return HttpResponse("data delete successfully")
        except:
            return HttpResponse("please enter a valid id")
    emps = Employee.objects.all()
    context = {
        "emp":emps
    }    
    
    return render(request,"remove_emp.html",context)

def filter_emp(request):
    if request.method=="POST":
        name = request.POST['name']
        role = request.POST['role']
        department = request.POST['department']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(name__icontains = name)
        if department:
            emps = emps.filter(department__name__icontains=department)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context = {
            "emps":emps
        }
        return render(request, "view_emp.html",context)
    elif request.method == "GET":
        return render(request,"filter_emp.html")
    else:
        return HttpResponse("an error occured")
