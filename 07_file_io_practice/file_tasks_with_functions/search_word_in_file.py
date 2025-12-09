def search_word(file_path, word):
    """Searches for a specific word in the given file and returns the line numbers where it is found."""
    with open(file_path, 'r') as file:
        content=file.read()
        if word in content.strip().lower() or word in content.strip().upper() or word in content.strip().capitalize():
            return True
        else:
            return False
word=input("Enter the word you want to search in the file: ")
found = search_word("notes.txt", word)
if found:
    print("The word was found in the file.")
else:
    print("The word was not found in the file.")
        