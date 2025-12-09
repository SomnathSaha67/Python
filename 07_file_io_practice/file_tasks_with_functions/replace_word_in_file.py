def replace_word(file_path, old_word, new_word):
    """Replaces all occurrences of old_word with new_word in the specified file."""
    with open(file_path, 'r') as file:
        content = file.read()
    
    updated_content = content.replace(old_word, new_word)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)
replace_word("notes.txt", "learning", "mastering")