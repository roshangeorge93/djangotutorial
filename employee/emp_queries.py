# ----for a department fetch the empolyee id and name---
Department.objects.get(id = 8)
Employee.objects.filter(d_id=dept).values('id','name')

# ----employee name and their respective departments----
emp = Employee.objects.select_related('d_id').all()
for emps in emp :
 print(f"{emps.name} belongs to {emps.d_id.name}")

# ----department location-----
dept =  Department.objects.select_related('location').all()
for depts in dept :
    print(f"{depts.name} is present in {depts.location.city}_{depts.location.state}_{depts.location.country}")


# ---Given an employee name get all the number assigned-----
emp = Employee.objects.get(name='Jeevan')
Contact.objects.filter(employee_id=emp).values('number')

# ----GIVEN NUMBER DISPLAY THE EMPLOYEE NAME----
con = Contact.objects.get(number='9123456738')
Employee.objects.filter(id=con.id).values('id','name')


