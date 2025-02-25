-- Get all distinct sem of student
q0 = Student.objects.values_list('Current_sem',flat=True).distinct().first()