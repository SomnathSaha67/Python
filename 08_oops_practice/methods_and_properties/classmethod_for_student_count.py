class Student:
    total_students=0
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        total_students+=1
    @classmethod
    def get_total_students(cls, total_students):
        return f"Total students: {}