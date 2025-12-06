# Simple Contact Book

# Step 1: Create initial contacts
num_of_contacts = int(input("Enter number of contacts: "))
contacts = {}

for i in range(num_of_contacts):
    name = input(f"Enter name of contact {i + 1}: ")
    phone = input(f"Enter phone number for {name}: ")
    more_info = input(
        f"Do you want to add more info for {name}?\n"
        " 1. yes\n"
        " 2. no\n"
        "Enter choice number: "
    ).strip()

    info = {}
    if more_info == "1":
        what_info = input(
            f"What additional infos do you want to add for {name}?\n"
            " 1. email\n"
            " 2. address\n"
            " 3. relation\n"
            " 4. profession\n"
            "Enter choices separated by commas: "
        )
        choices = what_info.split(",")
        for choice in choices:
            choice = choice.strip()
            if choice == "1":
                email = input(f"Enter email for {name}: ")
                info["email"] = email
            elif choice == "2":
                address = input(f"Enter address for {name}: ")
                info["address"] = address
            elif choice == "3":
                relation = input(f"Enter relation for {name}: ")
                info["relation"] = relation
            elif choice == "4":
                profession = input(f"Enter profession for {name}: ")
                info["profession"] = profession

    contacts[name] = {'phone': phone, 'info': info}
    print(f"Added contact {name}.")

# Step 2: Menu loop
while True:
    user_choice = input(
        "\nWhat do you want to do?\n"
        " 1. view contacts\n"
        " 2. update contacts\n"
        " 3. add contact\n"
        " 4. delete contact\n"
        " 5. exit\n"
        "Enter choice number: "
    ).strip()

    # View contacts
    if user_choice == "1":
        if not contacts:
            print("No contacts to display.")
        else:
            for contact, details in contacts.items():
                print(f"\nContact: {contact}")
                print(f"  Phone: {details['phone']}")
                info = details.get('info', {})
                for key, value in info.items():
                    print(f"  {key.capitalize()}: {value}")

    # Update contacts
    elif user_choice == "2":
        what_to_update = input(
            "What do you want to update?\n"
            " 1. phone number\n"
            " 2. additional info\n"
            " 3. both\n"
            "Enter choice number: "
        ).strip()

        contact_name = input("Enter the name of the contact to update: ")

        if contact_name in contacts:
            # Ensure 'info' dict exists
            if 'info' not in contacts[contact_name]:
                contacts[contact_name]['info'] = {}

            if what_to_update == "1" or what_to_update == "3":
                new_phone = input(f"Enter new phone number for {contact_name}: ")
                contacts[contact_name]['phone'] = new_phone

            if what_to_update == "2" or what_to_update == "3":
                info_key = input(
                    "Enter the info field(s) to update:\n"
                    " 1. email\n"
                    " 2. address\n"
                    " 3. relation\n"
                    " 4. profession\n"
                    "Enter choice numbers separated by commas: "
                )
                keys = info_key.split(",")
                for key in keys:
                    key = key.strip()
                    if key == "1":
                        new_email = input(f"Enter new email for {contact_name}: ")
                        contacts[contact_name]['info']['email'] = new_email
                    elif key == "2":
                        new_address = input(f"Enter new address for {contact_name}: ")
                        contacts[contact_name]['info']['address'] = new_address
                    elif key == "3":
                        new_relation = input(f"Enter new relation for {contact_name}: ")
                        contacts[contact_name]['info']['relation'] = new_relation
                    elif key == "4":
                        new_profession = input(f"Enter new profession for {contact_name}: ")
                        contacts[contact_name]['info']['profession'] = new_profession

            print(f"Updated contact {contact_name}.")
        else:
            print("Contact not found.")

    # Add contact
    elif user_choice == "3":
        name = input("Enter name of new contact: ")
        phone = input(f"Enter phone number for {name}: ")
        more_info = input(
            f"Do you want to add more info for {name}?\n"
            " 1. yes\n"
            " 2. no\n"
            "Enter choice number: "
        ).strip()

        info = {}
        if more_info == "1":
            what_info = input(
                f"What additional infos do you want to add for {name}?\n"
                " 1. email\n"
                " 2. address\n"
                " 3. relation\n"
                " 4. profession\n"
                "Enter choices separated by commas: "
            )
            choices = what_info.split(",")
            for choice in choices:
                choice = choice.strip()
                if choice == "1":
                    email = input(f"Enter email for {name}: ")
                    info["email"] = email
                elif choice == "2":
                    address = input(f"Enter address for {name}: ")
                    info["address"] = address
                elif choice == "3":
                    relation = input(f"Enter relation for {name}: ")
                    info["relation"] = relation
                elif choice == "4":
                    profession = input(f"Enter profession for {name}: ")
                    info["profession"] = profession

        contacts[name] = {'phone': phone, 'info': info}
        print(f"Added contact {name}.")

    # Delete contact or info
    elif user_choice == "4":
        contact_name = input("Enter the name of the contact to delete: ")
        if contact_name not in contacts:
            print("Contact not found.")
            continue

        what_to_delete = input(
            "Do you want to delete the entire contact or specific info?\n"
            " 1. entire contact\n"
            " 2. specific info\n"
            "Enter choice number: "
        ).strip()

        if what_to_delete == "1":
            del contacts[contact_name]
            print(f"Deleted contact {contact_name}.")
        elif what_to_delete == "2":
            info_dict = contacts[contact_name].get('info', {})
            if not info_dict:
                print("No additional info stored for this contact.")
            else:
                info_key = input(
                    "Enter the info field(s) to delete:\n"
                    " 1. email\n"
                    " 2. address\n"
                    " 3. relation\n"
                    " 4. profession\n"
                    "Enter choice numbers separated by commas: "
                )
                keys = info_key.split(",")
                for key in keys:
                    key = key.strip()
                    if key == "1" and 'email' in info_dict:
                        del info_dict['email']
                    elif key == "2" and 'address' in info_dict:
                        del info_dict['address']
                    elif key == "3" and 'relation' in info_dict:
                        del info_dict['relation']
                    elif key == "4" and 'profession' in info_dict:
                        del info_dict['profession']
                print(f"Updated contact {contact_name} after deletion.")
        else:
            print("Invalid delete choice.")

    # Exit
    elif user_choice == "5":
        print("Exiting the contact book.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
