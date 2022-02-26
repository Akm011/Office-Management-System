from django.contrib import admin
from employee_app.models import *

class EmployeeDetail(admin.ModelAdmin):
    list_display=('first_name','last_name','dept',)

class EmployeeRole(admin.ModelAdmin):
    list_display=('name',)

class EmployeeDepartment(admin.ModelAdmin):
    list_display=('name','location',)

# Register your models here.
admin.site.register(Employee,EmployeeDetail)
admin.site.register(Role,EmployeeRole)
admin.site.register(Department,EmployeeDepartment)