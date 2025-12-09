# Daily Notes Logger with File Persistence

NOTES_FILE = "notes.txt"


def add_note():
    note = input("Enter your note: ")
    # You can keep time simple: just date or date+time
    from datetime import datetime

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    line = f"{timestamp} - {note}\n"
    with open(NOTES_FILE, "a") as f:
        f.write(line)
    print("Note added.")


def view_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            data = f.read()
            if not data:
                print("No notes yet.")
            else:
                print("\n--- Your Notes ---")
                print(data, end="")
    except FileNotFoundError:
        print("No notes file found yet. Add a note first.")


def clear_notes():
    confirm = input("Are you sure you want to clear all notes? (yes/no): ").strip().lower()
    if confirm == "yes":
        # Overwrite with empty content
        with open(NOTES_FILE, "w") as f:
            pass
        print("All notes cleared.")
    else:
        print("Clear cancelled.")


def main():
    while True:
        print(
            "\nDaily Notes\n"
            " 1. Add a new note\n"
            " 2. View all notes\n"
            " 3. Clear all notes\n"
            " 4. Exit"
        )
        choice = input("Enter choice number: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            clear_notes()
        elif choice == "4":
            print("Exiting Daily Notes.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
main()