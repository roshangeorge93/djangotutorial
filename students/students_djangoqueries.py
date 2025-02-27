
# students app:

# -- List all students belonging to sem1
# select * from student 
# where current_sem='1';

# ----DJANGO EQUIVALENT-------
sem1_students=Student.objects.filter(current_sem=1).values('name')
for student in sem1_students:
   print(student)

# ----------------------------------------------------------------------------------------------------------------------

# -- Get all marks of a student (given usn) for a particular subject
# SELECT
# 	result.marks
# FROM
# 	result
# 	JOIN student ON result.student_id = student.id
# 	JOIN subject ON result.subject_id = subject.id
# WHERE
# 	student.usn = 'vv001'
# 	AND subject.name = 'student2';

# ----DJANGO EQUIVALENT-------
marks=Result.objects.select_related('student','subject').filter(student_id__usn='vv001',subject_id__name='subject2').values('marks').first()
print(f"{marks['marks']}")

# ----------------------------------------------------------------------------------------------------------------------

# -- Get all marks of a student given usn for the latest semester 
# SELECT
# 	result.marks
# FROM
# 	result
# 	join 
# 	student
# on
# 	result.student_id = student.id
# 	AND student.usn = 'vv404' AND
# 	RESULT.sem_id=student.current_sem;

# ----DJANGO EQUIVALENT------
latest_sem_marks=Result.objects.select_related('student').filter(student_id__usn='vv404',semester_id=F('student__current_sem')).values('marks')
for result in latest_sem_marks:
     print(result)
# ----------------------------------------------------------------------------------------------------------------------

# -- What all semester has the student attended
# SELECT string_agg(sem::TEXT,',') as total_sems_attended
# FROM generate_series(1,(select current_sem from student WHERE student.name='student5')) AS sem;

# ----DJANGO EQUIVALENT-------
cur_sem=Student.objects.filter(usn='vv404').values_list('current_sem',flat=True).first()
all_sems=list(range(1,cur_sem+1))
print(all_sems)

# ----------------------------------------------------------------------------------------------------------------------

# -- Get the total percentage of marks for a student in a sem
# select round((sum(result.marks::NUMERIC) / count(result.subject_id)),2) as percentage from result,student  where result.student_id=student.id AND result.sem_id=2 AND student.usn='vv001';

# ----DJANGO EQUIVALENT-------

print(Student.objects.filter(usn='vv404', result__semester__semester_number=1).annotate(t_marks=ExpressionWrapper((Sum('result__marks') / Count('result__subject')),output_field=FloatField())).values())

# ----------------------------------------------------------------------------------------------------------------------
# -- Get the total percentage of marks for a student in each semester.

# SELECT
# 	RESULT.sem_id,
# 	round((sum(result.marks)::NUMERIC / count(result.subject_id)), 2) AS percentage
# FROM
# 	result,
# 	student
# WHERE
# 	result.student_id = student.id
# 	AND student.usn = 'vv001'
# GROUP BY
# 	RESULT.sem_id;

# ----DJANGO EQUIVALENT-------
percentage=Student.objects.filter(usn='vv404',).annotate(t_percentage=ExpressionWrapper((Sum('result__marks') / Count('result__subject')),output_field=FloatField())).values('result__semester','t_percentage')
for i in percentage:
         print(i)

# ----------------------------------------------------------------------------------------------------------------------

# -- Get total percentage of marks for a student
# SELECT
# 	 round  (sum(result.marks)::NUMERIC / count(result.subject_id), 2) AS total_percentage
# FROM
# 	result,
# 	student
# WHERE
# 	result.student_id = student.id
# 	AND student.usn = 'vv001';

# ----DJANGO EQUIVALENT-------
percentage = Student.objects.filter(usn='vv001',).annotate(t_percentage=ExpressionWrapper((Sum('result__marks') / Count('result__subject')),output_field=FloatField())).values('t_percentage')
print(percentage)
# ----------------------------------------------------------------------------------------------------------------------
