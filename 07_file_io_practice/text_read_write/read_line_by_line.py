with open("notes.txt","r") as file:
    number_of_lines=int(input("Enter the number of lines to read: "))
    a=file.readlines()
    if number_of_lines > 0:
        if number_of_lines <= len(a):
            for i in range(number_of_lines):
                print(a[i], end="")
        else:
            print("The file has fewer lines than requested.")
    else:
        print("Please enter a positive integer.")