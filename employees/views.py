from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from django.template import loader


def employee(request,employee_id):
    Employee_details=Employee.objects.filter(id=employee_id).select_related('department__l').all()
    context = {
         "Employee_details": Employee_details,
    }
    return render(request, "Employee_details.html", context)
  









# def index(request):
#     employee_list = Employee.objects.select_related('department__l').all()
    
#     context = {
#         "employee_list": employee_list,
#     }
    
#     return render(request, "index.html", context)


# def test(request):
    
#     return render(request,"test.html")





def employee_list(request):
   
    all_names = Employee.objects.values_list('Name', flat=True).distinct()
    all_designations = Employee.objects.values_list('Designation', flat=True).distinct()
    all_addresses = Employee.objects.values_list('department__l__l_country', flat=True).distinct()
    all_emails = Employee.objects.values_list('Email', flat=True).distinct()

    
    name_filter = request.GET.get('name', '')
    designation_filter = request.GET.get('designation', '')
    address_filter = request.GET.get('address', '')
    email_filter = request.GET.get('email', '')

   
    employees = Employee.objects.all()
    if name_filter:
        employees = employees.filter(Name=name_filter)
    if designation_filter:
        employees = employees.filter(Designation=designation_filter)
    if address_filter:
        employees = employees.filter(department__l__l_country=address_filter)
    if email_filter:
        employees = employees.filter(Email=email_filter)

    context = {
        'employee_list': employees,
        'all_names': all_names,
        'all_designations': all_designations,
        'all_addresses': all_addresses,
        'all_emails': all_emails,
        'selected_name': name_filter,
        'selected_designation': designation_filter,
        'selected_address': address_filter,
        'selected_email': email_filter
    }
    return render(request, 'index.html', context)
