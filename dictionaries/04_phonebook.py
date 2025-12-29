num_of_contacts=int(input("Enter number of contacts to add to the phonebook: "))
phonebook={}
for i in range(num_of_contacts):
    name=input("Enter name for contact {}: ".format(i+1))
    phone_number=input("Enter phone number for contact {}: ".format(i+1))
    phonebook[name]=phone_number
print("Phonebook Dictionary:")
for name, number in phonebook.items():
    print("{}: {}".format(name, number))
#search for a contact
search_name=input("Enter the name of the contact to search: ")
if search_name in phonebook:
    print("Phone number of {}: {}".format(search_name, phonebook[search_name]))
else:
    search_by_number=input("Contact not found. Enter phone number to search by number: ")
    found=False
    for name, number in phonebook.items():
        if number==search_by_number:
            print("Contact found: {} with phone number {}".format(name, number))
            found=True
            break
    if not found:
        print("No contact found with phone number {}".format(search_by_number))
#add a new contact
new_name=input("Enter name for new contact to add: ")
new_number=input("Enter phone number for new contact to add: ")
phonebook[new_name]=new_number
print("Updated Phonebook Dictionary:")
for name, number in phonebook.items():
    print("{}: {}".format(name, number))
#delete a contact
delete_name=input("Enter the name of the contact to delete: ")
if delete_name in phonebook:
    del phonebook[delete_name]
    print("Contact {} deleted.".format(delete_name))
else:
    delete_by_number=input("Contact not found. Enter phone number to delete by number: ")
    found=False
    for name, number in list(phonebook.items()):
        if number==delete_by_number:
            del phonebook[name]
            print("Contact {} with phone number {} deleted.".format(name, number))
            found=True
            break
    if not found:
        print("No contact found with phone number {}".format(delete_by_number))
print("Final Phonebook Dictionary:")
for name, number in phonebook.items():
    print("{}: {}".format(name, number))