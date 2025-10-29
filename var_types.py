#Ask the user for their name (string), age (int), height (float), and whether they are a student (yes/no, converted to boolean).
#Print each value and its data type using the type() function.

# Get user inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student_input = input("Are you a student? (Y/N): ")
if is_student_input in ['Y', 'y']:
    is_student = True
else:
    is_student = False      
# Print values and their data types
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")    
