with open("temp.txt", "w+") as file:
    file.write("This file is opened in 'w+' mode, which allows both writing and reading.\n")
    file.write("The file is truncated to zero length when opened.\n")
    file.write("You can write new content and then read it back.\n")
    
    # Move the cursor back to the beginning of the file before reading
    file.seek(0)
    
    content = file.read()
    print("Content of the file after writing:")
    print(content)