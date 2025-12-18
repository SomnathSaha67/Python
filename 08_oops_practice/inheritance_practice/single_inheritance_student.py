class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} I am also a student with ID: {self.student_id}."
number_of_students = int(input("Enter number of students: "))
students = []
for _ in range(number_of_students):
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    student_id = input("Enter student's ID: ")
    student = Student(name, age, student_id)
    students.append(student)
for student in students:
    print(student.introduce())