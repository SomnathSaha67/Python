#Create a dictionary to store information about a student (name, roll, branch, year).
#Print each key-value pair.
#Demonstrate adding, updating, and deleting an entry from the dictionary.

# Creating a dictionary to store student information
n=int(input("Enter number of students: "))
students = {}
for i in range(n):
    name = input("Enter student name: ")
    roll = input("Enter student roll number: ")
    branch = input("Enter student branch: ")
    year = input("Enter student year: ")
    students[roll] = {'name': name, 'branch': branch, 'year': year}
# Printing each key-value pair
print("\nStudent Information:")
for roll, info in students.items():
    print(f"Roll Number: {roll}, Name: {info['name']}, Branch: {info['branch']}, Year: {info['year']}")
# Adding a new entry
new_roll = input("\nEnter new student roll number to add: ")
new_name = input("Enter new student name: ")
new_branch = input("Enter new student branch: ")
new_year = input("Enter new student year: ")
students[new_roll] = {'name': new_name, 'branch': new_branch, 'year': new_year}
print(f"\nAdded student with roll number {new_roll}.")
# Updating an existing entry
update_roll = input("\nEnter student roll number to update: ")
if update_roll in students:
    update_name = input("Enter new name: ")
    update_branch = input("Enter new branch: ")
    update_year = input("Enter new year: ")
    students[update_roll] = {'name': update_name, 'branch': update_branch, 'year': update_year}
    print(f"\nUpdated student with roll number {update_roll}.")
else:
    print(f"\nStudent with roll number {update_roll} not found.")
# Deleting an entry
delete_roll = input("\nEnter student roll number to delete: ")
if delete_roll in students:
    del students[delete_roll]
    print(f"\nDeleted student with roll number {delete_roll}.")
else:
    print(f"\nStudent with roll number {delete_roll} not found.")
