class ToDo_Item:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        status = 'Completed' if self.completed else 'Incomplete'
        return f'ToDoItem(title="{self.title}", description="{self.description}", status="{status}")'
number_of_items = int(input("Enter number of to-do items: "))
todo_items = []
for _ in range(number_of_items):
    title = input("Enter title of the to-do item: ")
    description = input("Enter description (or press Enter to skip): ") or ''
    item = ToDo_Item(title, description)
    todo_items.append(item)
for item in todo_items:
    print(f"\n{item}")
    mark_complete = input("Mark this item as completed? (yes/no): ").strip().lower()
    if mark_complete == 'yes':
        item.mark_completed()
    print(f"Updated Item: {item}")
    