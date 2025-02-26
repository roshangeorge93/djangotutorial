# STUDENT

# 1) List all students belonging to Sem7

from student.models import Student
a = Student.objects.filter(current_sem=7)
print(a.values())



# 2) Get all marks of a student given USN for a particular subject

from student.models import Result
usn_value = 'USN001'
subject_value = 'Mathematics'

results = Result.objects.filter(student__USN=usn_value, subject__name=subject_value).values('student__USN','marks')

print(results)



# 3) What all semesters has the student attended

from student.models import Result, Student
sem_numbers = Result.objects.filter(student__USN='USN002').values('semester_id').distinct()



# 4)Get all marks of a student given USN for the current semester


from student.models import Result, Student, Subject

usn_value='USN001'
current_sem_num='7'
results = Result.objects.filter(student__USN=usn_value, student__current_sem=current_sem_num).values('student__USN','marks')
print(results)


# 5) Get the total percentage of marks for a student in a semester

from student.models import Results, Student, Subject
usn_value = 'USN001'
sem_number = 1
