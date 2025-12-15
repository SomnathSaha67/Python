class Student:
    def __init__(self, name, age, marks):
        self.name=name
        self.age=age
        self.marks=marks
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
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
    student.print_details()
