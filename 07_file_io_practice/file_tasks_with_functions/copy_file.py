def copy_file(source_path, destination_path):
    """Copies the content from source_path to destination_path."""
    with open(source_path, 'r') as source_file:
        content = source_file.read()
    
    with open(destination_path, 'w') as dest_file:
        dest_file.write(content)
copy_file("notes.txt", "notes_copy.txt")