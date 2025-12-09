with open("notes.txt","w") as file:
   number_of_lines=int(input("Enter the number of lines you want to write to the file: "))
   for i in range(number_of_lines):
       line=input(f"Enter line {i+1}: ")
       file.write(line + "\n")