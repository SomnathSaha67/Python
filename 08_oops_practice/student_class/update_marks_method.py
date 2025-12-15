class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def update_marks(self, new_marks):  
        index=int(input("Enter the index of the subject to update marks: "))
        if 0 <= index < len(self.marks):
            self.marks[index] = new_marks
        else:
            print("Invalid index. No update made.")
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
    print(f"Current marks for {student.name}: {student.marks}")
    new_mark=float(input(f"Enter new mark to update for {student.name}: "))
    student.update_marks(new_mark)
    print(f"Updated marks for {student.name}: {student.marks}")