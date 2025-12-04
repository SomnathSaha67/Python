string="I love programming in Python"
search_substring=input("Enter substring to find: ")
index=string.find(search_substring)
if index != -1:
    print(f"Substring '{search_substring}' found at index: {index}")
else:
    print(index)