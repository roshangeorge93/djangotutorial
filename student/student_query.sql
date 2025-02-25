-- Get all distinct sem of student
q0 = Student.objects.values_list('Current_sem',flat=True).distinct().first()




-- list all student belonging to sem 1
q1=Student.objects.filter(Current_sem='1').values_list('Name',flat=True).first()



-- get all marks of a student given usn for the latest seem

cur_sem=Student.objects.filter(Usn='vv005').values_list('Current_sem',flat=True).first()
q3=Marks.objects.filter(Student_Id__Usn='vv005').get(Sem_Id__Sem=cur_sem)
print(q3.Marks)

-- get all marks of a student given usn for a particular subject
sub=Subject.objects.filter(Sub_name='DS').values_list('Sub_Id',flat=True).first()
q4=Marks.objects.filter(Student_Id__Usn='vv003').get(Sub_Id=sub)
print(q4.Marks)



 
-- get the total percentage of marks for a student in each sem





-- get total percentage of student of all sem