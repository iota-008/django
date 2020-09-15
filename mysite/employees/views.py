from django.shortcuts import render
from django.http import HttpResponse 
from .models import employee
from django.http import Http404

# Create your views here.

def home(request):
    # return HttpResponse("Welcome Home")
    employees = employee.objects.all()
    return render(request,'home.html',{'employees':employees})


def employee_details(requet, employee_id):
    # return HttpResponse(f'Employee ID is {employee_id}')    
    try:
        emp = employee.objects.get(id=employee_id)
    except employee.DoesNotExist:
        raise Http404
    return render(requet, 'EmployeeDetails.html', {'employee': emp})
    