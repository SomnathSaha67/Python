with open("log.txt","r+") as file:
    content = file.read()
    print("Current content of the file:")
    print(content)
    
    file.write("Adding a new line using 'r+' mode.\n")
    file.write("This line is added at the end of the existing content.\n")
with open("log.txt","r+") as file:
    updated_content = file.read()
    print("Updated content of the file:")
    print(updated_content)
    file.seek(0)
    file.write("Overwriting the beginning of the file using 'r+' mode.\n")
with open("log.txt","r") as file:
    final_content = file.read()
    print("Final content of the file after overwriting:")
    print(final_content)