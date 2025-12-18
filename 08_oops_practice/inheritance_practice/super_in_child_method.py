class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    def greeting(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and I work as an employee."
class Manager(Employee):
    def __init__(self, department):
        super().__init__(employee_id, salary)
        self.department = department
    def introduce(self):
        super_intro = super().greeting()
        print(f"{super_intro} I am also a manager of the {self.department} department.")
    def print_manager_info(self):
        return (f"Manager Name: {self.name}, Age: {self.age}, "
                f"Employee ID: {self.employee_id}, Salary: {self.salary}, "
                f"Department: {self.department}")
number_of_employees = int(input("Enter number of employees: "))
employees = []
for _ in range(number_of_employees):
    name = input("Enter employee's name: ")
    age = int(input("Enter employee's age: "))
    employee_id = input("Enter employee's ID: ")
    salary = float(input("Enter employee's salary: "))
    department = input("Enter manager's department: ")
    manager = Manager(department)
    employees.append(manager)
for employee in employees:
    print(employee.introduce())
    print(employee.print_manager_info())
