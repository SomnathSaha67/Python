with open("notes.txt", "r") as file:
    number_of_chars=int(input("Enter the number of characters to read: "))
    if number_of_chars > 0:
        if number_of_chars <= len(file.read()):
            file.seek(0)  # Reset file pointer to the beginning
            content = file.read(number_of_chars)
            print(content)
        else:
            print("The file has fewer characters than requested.")
    else:
        print("Please enter a positive integer.")