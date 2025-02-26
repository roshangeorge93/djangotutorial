from employees.models import Employee,Contact,Department


# ---list all emplyoee and contact number
q0=Contact.objects.select_related('Emp__department').all()
for q in q0:
    print(f"{q.Emp.Name} {q.Number} {q.Emp.department.department_id}")


# --get contact details by giving name
q1=Contact.objects.filter(Emp__Name='e1')
for q in q1:
    print(q.Number)