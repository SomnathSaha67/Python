# Student Grade Manager with File Persistence

STUDENTS_FILE = "students.txt"


def load_students_from_file():
    students = []
    try:
        with open(STUDENTS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 5:
                    continue
                name = parts[0]
                roll = parts[1]
                try:
                    m1 = float(parts[2])
                    m2 = float(parts[3])
                    m3 = float(parts[4])
                except ValueError:
                    continue

                total = m1 + m2 + m3
                average = total / 3

                student = {
                    "name": name,
                    "roll": roll,
                    "marks": {
                        "Maths": m1,
                        "Science": m2,
                        "English": m3,
                    },
                    "total": total,
                    "average": average,
                }
                students.append(student)
    except FileNotFoundError:
        students = []
    return students


def save_students_to_file(students):
    with open(STUDENTS_FILE, "w") as f:
        for s in students:
            m1 = s["marks"]["Maths"]
            m2 = s["marks"]["Science"]
            m3 = s["marks"]["English"]
            line = f"{s['name']},{s['roll']},{m1},{m2},{m3}\n"
            f.write(line)


def find_student_index_by_roll(students, roll_to_find):
    for index in range(len(students)):
        if students[index]["roll"] == roll_to_find:
            return index
    return -1


def view_students(students):
    if not students:
        print("No students to display.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"\nName: {s['name']}")
        print(f"Roll: {s['roll']}")
        print("Marks:")
        for subject, mark in s["marks"].items():
            print(f"  {subject}: {mark}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']}")
        if s["average"] >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


def add_student(students):
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
            "English": m3,
        },
        "total": total,
        "average": average,
    }
    students.append(student)
    print(f"Added student {name} (Roll: {roll}).")


def update_student_marks(students):
    print("\n--- Update Student Marks ---")
    roll_to_update = input("Enter roll number of student to update: ")
    index = find_student_index_by_roll(students, roll_to_update)

    if index == -1:
        print("Student not found.")
        return

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
    options = [o.strip() for o in opt.split(",")]

    if "4" in options:
        # update all
        s["marks"]["Maths"] = float(input("New marks in Maths: "))
        s["marks"]["Science"] = float(input("New marks in Science: "))
        s["marks"]["English"] = float(input("New marks in English: "))
    else:
        if "1" in options:
            s["marks"]["Maths"] = float(input("New marks in Maths: "))
        if "2" in options:
            s["marks"]["Science"] = float(input("New marks in Science: "))
        if "3" in options:
            s["marks"]["English"] = float(input("New marks in English: "))

    m1 = s["marks"]["Maths"]
    m2 = s["marks"]["Science"]
    m3 = s["marks"]["English"]
    s["total"] = m1 + m2 + m3
    s["average"] = s["total"] / 3

    print("Updated marks and recalculated total and average.")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll_to_delete = input("Enter roll number of student to delete: ")
    index = find_student_index_by_roll(students, roll_to_delete)

    if index == -1:
        print("Student not found.")
    else:
        removed = students.pop(index)
        print(f"Deleted student {removed['name']} (Roll: {removed['roll']}).")


def show_topper(students):
    if not students:
        print("No students available.")
        return
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


def main():
    students = load_students_from_file()
    print("Loaded students from file.")

    while True:
        print(
            "\nWhat do you want to do?\n"
            " 1. View all students\n"
            " 2. Add a new student\n"
            " 3. Update a student's marks\n"
            " 4. Delete a student\n"
            " 5. Show topper (highest average)\n"
            " 6. Save & Exit"
        )
        choice = input("Enter choice number: ").strip()

        if choice == "1":
            view_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            update_student_marks(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            show_topper(students)
        elif choice == "6":
            save_students_to_file(students)
            print("Students saved. Exiting Student Grade Manager.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
main()
