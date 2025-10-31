#Maintain a dictionary where keys are student names and values are their marks.
#Allow adding/updating students and their marks, and display the average score.

# Creating an empty gradebook dictionary
gradebook = {}  
while True: 
    print("\nGradebook Menu:")
    print("1. Add/Update Student Marks")
    print("2. Display Average Score")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))
        gradebook[name] = marks
        print(f"Marks for '{name}' added/updated.")
        
    elif choice == '2':
        if gradebook:
            average_score = sum(gradebook.values()) / len(gradebook)
            print(f"The average score of the class is: {average_score:.2f}")
        else:
            print("No student records found.")
            
    elif choice == '3':
        print("Exiting Gradebook. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
# Printing the current gradebook
print("\nCurrent Gradebook:")
for name, marks in gradebook.items():
    print(f"{name}: {marks}")
