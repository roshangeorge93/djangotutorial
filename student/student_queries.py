# 1)Give student details of sem 1 
students = Student.objects.filter(current_sem='1')



# 2. Semesters student have attended
semesters = Result.objects.filter(student__usn='CS101').values('sem').distinct()
semester_ids = [semester['sem'] for semester in semesters]
print(f"Semesters attended by student with USN 'CS101': {', '.join(map(str, semester_ids))}")


# 3. print every student every sem average_marks

from django.db.models import Avg
from student.models import Result, student, semester

average_marks = Result.objects.values('student_id', 'sem_id') \
                               .annotate(average_marks=Avg('marks')) \
                               .order_by('student', 'sem')

for entry in average_marks:
    student_instance = student.objects.get(id=entry['student_id'])
    semester_instance = semester.objects.get(id=entry['sem_id'])
    print(f"Student: {student_instance.name}, Semester: {semester_instance.id}, Average Marks: {entry['average_marks']}")
