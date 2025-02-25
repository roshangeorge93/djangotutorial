---list all emplyoee and contact number
q0=Contact.objects.select_related('Emp__department').all()
for q in q0:
    print(f"{q.Emp.Name} {q.Number} {q.Emp.department.department_id}")