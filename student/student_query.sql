-- Get all distinct sem of student
q0 = Student.objects.values_list('Current_sem',flat=True).distinct().first()




-- list all student belonging to sem 1
q1=Student.objects.filter(Current_sem='1').values_list('Name',flat=True).first()
