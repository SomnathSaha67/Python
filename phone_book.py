#Build a simple phonebook application.
#Let the user add, search, update, and delete contacts (name: phone number pairs) using a loop.

# Creating an empty phonebook dictionary
phonebook = {}  
while True: 
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        phonebook[name] = phone_number
        print(f"Contact '{name}' added.")
        
    elif choice == '2':
        name = input("Enter contact name to search: ")
        if name in phonebook:
            print(f"Contact found: {name} - {phonebook[name]}")
        else:
            print(f"Contact '{name}' not found.")
            
    elif choice == '3':
        name = input("Enter contact name to update: ")
        if name in phonebook:
            new_phone_number = input("Enter new phone number: ")
            phonebook[name] = new_phone_number
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found.")
            
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")
            
    elif choice == '5':
        print("Exiting Phonebook. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
# Printing the current phonebook
print("\nCurrent Phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")