#Maintain a list of student names.
#Allow the user to:
#Add a name
#Remove a name
#Search for a name
#List all names alphabetically
#Loop this menu until the user chooses to exit.

student_names = []
while True:
    print("\nStudent Manager Menu:")
    print("1. Add a name")
    print("2. Remove a name")
    print("3. Search for a name")
    print("4. List all names alphabetically")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        name_to_add = input("Enter the name to add: ")
        student_names.append(name_to_add)
        print(f"{name_to_add} has been added.")        
    elif choice == '2':
        name_to_remove = input("Enter the name to remove: ")
        if name_to_remove in student_names:
            student_names.remove(name_to_remove)
            print(f"{name_to_remove} has been removed.")
        else:
            print(f"{name_to_remove} not found in the list.")
    elif choice == '3':
        name_to_search = input("Enter the name to search for: ")
        if name_to_search in student_names:
            print(f"{name_to_search} is in the list.")
        else:
            print(f"{name_to_search} not found in the list.")
    elif choice == '4':
        print("Student Names (Alphabetically):")
        for name in sorted(student_names):
            print(name)
    elif choice == '5':
        print("Exiting Student Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")