# Simple Student Grade Manager

students = []  # list of dicts: {'name': ..., 'roll': ..., 'marks': {...}, 'total': ..., 'average': ...}

# Step 1: Optionally take some initial students
num_students = int(input("Enter number of students to add initially: "))

for i in range(num_students):
    print(f"\n--- Enter details for student {i + 1} ---")
    name = input("Name: ")
    roll = input("Roll number: ")

    # For simplicity, use three fixed subjects
    m1 = float(input("Marks in Maths: "))
    m2 = float(input("Marks in Science: "))
    m3 = float(input("Marks in English: "))

    total = m1 + m2 + m3
    average = total / 3

    student = {
        "name": name,
        "roll": roll,
        "marks": {
            "Maths": m1,
            "Science": m2,
            "English": m3
        },
        "total": total,
        "average": average
    }

    students.append(student)
    print(f"Added student {name} (Roll: {roll}).")

# Helper: find index of student by roll number
def find_student_index_by_roll(roll_to_find):
    for index in range(len(students)):
        if students[index]["roll"] == roll_to_find:
            return index
    return -1

# Step 2: Menu loop
while True:
    print(
        "\nWhat do you want to do?\n"
        " 1. View all students\n"
        " 2. Add a new student\n"
        " 3. Update a student's marks\n"
        " 4. Delete a student\n"
        " 5. Show topper (highest average)\n"
        " 6. Exit"
    )
    choice = input("Enter choice number: ").strip()

    # View all students
    if choice == "1":
        if not students:
            print("No students to display.")
        else:
            print("\n--- Student Records ---")
            for s in students:
                print(f"\nName: {s['name']}")
                print(f"Roll: {s['roll']}")
                print("Marks:")
                for subject, mark in s["marks"].items():
                    print(f"  {subject}: {mark}")
                print(f"Total: {s['total']}")
                print(f"Average: {s['average']}")
                if s['average'] >= 40:
                    print("Result: PASS")
                else:
                    print("Result: FAIL")

    # Add a new student
    elif choice == "2":
        print("\n--- Add New Student ---")
        name = input("Name: ")
        roll = input("Roll number: ")

        m1 = float(input("Marks in Maths: "))
        m2 = float(input("Marks in Science: "))
        m3 = float(input("Marks in English: "))

        total = m1 + m2 + m3
        average = total / 3

        student = {
            "name": name,
            "roll": roll,
            "marks": {
                "Maths": m1,
                "Science": m2,
                "English": m3
            },
            "total": total,
            "average": average
        }

        students.append(student)
        print(f"Added student {name} (Roll: {roll}).")

    # Update marks
    elif choice == "3":
        print("\n--- Update Student Marks ---")
        roll_to_update = input("Enter roll number of student to update: ")
        index = find_student_index_by_roll(roll_to_update)

        if index == -1:
            print("Student not found.")
        else:
            s = students[index]
            print(f"Updating marks for {s['name']} (Roll: {s['roll']})")

            print(
                "Which subject(s) do you want to update?\n"
                " 1. Maths\n"
                " 2. Science\n"
                " 3. English\n"
                " 4. All three"
            )
            opt = input("Enter choice number(s) separated by commas: ")

            options = opt.split(",")
            for o in options:
                o = o.strip()
                if o == "1" or opt.strip() == "4":
                    new_m1 = float(input("New marks in Maths: "))
                    s["marks"]["Maths"] = new_m1
                if o == "2" or opt.strip() == "4":
                    new_m2 = float(input("New marks in Science: "))
                    s["marks"]["Science"] = new_m2
                if o == "3" or opt.strip() == "4":
                    new_m3 = float(input("New marks in English: "))
                    s["marks"]["English"] = new_m3

            # Recalculate total and average
            m1 = s["marks"]["Maths"]
            m2 = s["marks"]["Science"]
            m3 = s["marks"]["English"]
            s["total"] = m1 + m2 + m3
            s["average"] = s["total"] / 3

            print("Updated marks and recalculated total and average.")

    # Delete a student
    elif choice == "4":
        print("\n--- Delete Student ---")
        roll_to_delete = input("Enter roll number of student to delete: ")
        index = find_student_index_by_roll(roll_to_delete)

        if index == -1:
            print("Student not found.")
        else:
            removed = students.pop(index)
            print(f"Deleted student {removed['name']} (Roll: {removed['roll']}).")

    # Show topper
    elif choice == "5":
        if not students:
            print("No students available.")
        else:
            topper = students[0]
            for s in students[1:]:
                if s["average"] > topper["average"]:
                    topper = s
            print("\n--- Topper ---")
            print(f"Name: {topper['name']}")
            print(f"Roll: {topper['roll']}")
            print(f"Average: {topper['average']}")
            print("Marks:")
            for subject, mark in topper["marks"].items():
                print(f"  {subject}: {mark}")

    # Exit
    elif choice == "6":
        print("Exiting Student Grade Manager.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
