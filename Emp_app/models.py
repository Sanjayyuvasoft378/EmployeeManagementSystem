from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    mobileNo = models.CharField(max_length=10)
    salary = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    bonus = models.IntegerField(default=0)
    hireDate = models.DateField()
    def __str__(self):
        return "%s %s %s" %(self.name, self.role, self.mobileNo)