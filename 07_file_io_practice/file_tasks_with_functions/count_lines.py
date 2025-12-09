def count_lines(file_path):
    """Counts the number of lines in the specified file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)
line_count = count_lines("notes.txt")
print(f"The file 'notes.txt' has {line_count} lines.")