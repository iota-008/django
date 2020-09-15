from django.contrib import admin
from .models import employee,AvailableJobs
# Register your models here.
@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone_number','gender']


@admin.register(AvailableJobs)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['job_name']
    