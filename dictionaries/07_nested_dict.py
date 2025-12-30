num_of_subjects=int(input("Enter number of subjects: "))
subjects={}
for i in range(num_of_subjects):
    subject_name=input("Enter name of subject {}: ".format(i+1))
    num_of_students=int(input("Enter number of students in {}: ".format(subject_name)))
    students={}
    for j in range(num_of_students):
        student_name=input("Enter name of student {} in {}: ".format(j+1, subject_name))
        grade=float(input("Enter grade for {}: ".format(student_name)))
        students[student_name]=grade
    subjects[subject_name]=students
print("Subjects Dictionary with Students and Grades:")
for subject, students in subjects.items():
    print("Subject: {}".format(subject))
    for student, grade in students.items():
        print("  {}: {:.2f}".format(student, grade))
    