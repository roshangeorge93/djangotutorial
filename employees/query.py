from employees.models import Employee,Contact,Department


# ---list all emplyoee and contact number
q0=Contact.objects.select_related('Emp__department').all()
for q in q0:
    print(f"{q.Emp.Name} {q.Number} {q.Emp.department.department_id}")


# --get contact details by giving name
q1=Contact.objects.filter(Emp__Name='e1')
for q in q1:
    print(q.Number)

# --get employee name by giving number
q2=Employee.objects.filter(contact__Number='1234567891')
for q in q2:
    print(q.Name)


# --location city_state_country
q3=Employee.objects.select_related('department__l').all()
for q in q3:
    print(f"{q.Name} { q.department.department_id} {q.department.department_name} {q.department.l.l_city}_{q.department.l.l_state}_{q.department.l.l_country}")
