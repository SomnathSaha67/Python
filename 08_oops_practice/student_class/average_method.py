class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
number_of_students=int(input("Enter number of students: "))
students=[]
for _ in range(number_of_students):
    name=input("Enter student name: ")
    age=int(input("Enter student age: "))
    number_of_subjects=int(input("Enter number of subjects: "))
    marks=[]
    for _ in range(number_of_subjects):
        mark=float(input("Enter mark: "))
        marks.append(mark)
    student=Student(name, age, marks)
    students.append(student)
for student in students:
    avg=student.average_marks()
    print(f"Name: {student.name}, Average Marks: {avg}")
