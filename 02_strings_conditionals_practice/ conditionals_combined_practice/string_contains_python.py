string=input("Enter a string: ")
search_substring="python"
if search_substring.lower() in string.lower():
    print(f"Nice! The string contains '{search_substring}'")
else:
    print(f"Sorry, the string does not contain '{search_substring}'")