string=input("Enter a string: ")
character_index=int(input("Enter the index of the character you want to access: "))
if 0 <= character_index < len(string):
    print(f"The character at index {character_index} of {string} is '{string[character_index]}'.")
else:
    print("Index out of range.")
starting_parent_index=int(input("Enter the starting index of the substring: "))
ending_parent_index=int(input("Enter the ending index of the substring: "))
if 0 <= starting_parent_index < len(string) and 0 <= ending_parent_index <= len(string) and starting_parent_index < ending_parent_index:
    print(f"The substring from index {starting_parent_index} to {ending_parent_index} is '{string[starting_parent_index:ending_parent_index]}'.")
else:
    print("Invalid substring indices.")