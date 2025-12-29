gradesheet={}
num_students=int(input("Enter number of students: "))
for i in range(num_students):
    name=input("Enter name of student {}: ".format(i+1))
    num_of_subjects=int(input("Enter number of subjects for {}: ".format(name)))
    grades=[]
    for j in range(num_of_subjects):
        grade=float(input("Enter grade for subject {}: ".format(j+1)))
        grades.append(grade)
    gradesheet[name]=grades
print("Student Gradesheet:")
for student, grades in gradesheet.items():
    print("{}: {}".format(student, grades))
#average grades
print("Average Grades:")
for student, grades in gradesheet.items():
    average=sum(grades)/len(grades) if grades else 0
    print("{}: {:.2f}".format(student, average))    
    