# 1) -- Select * from employee

from employee.models import Employee
employees = Employee.objects.all()
employees.values()

# -----------------------------------------------------------------------------------------------------------------

# 2) -- To get list of contact numbers given eid


from employee.models import Employee, Contact_details
employee_id = '3'

contact_details = Contact_details.objects.filter(id=employee_id).select_related('employee').values('id','number')

for detail in contact_details:
	print(detail)

# -----------------------------------------------------------------------------------------------------------------

# 3) -- To get employee details based on the contact number


from employee.models import Employee, Contact_details
contact_number = 9886468304

employees = Employee.objects.filter(Contact_details__number=contact_number).values('id','name','email','designation','salary','experience','department_id')

for employee in employees:
    print(employee)





## -----------------------------------------------------------------------------------------------------------------
