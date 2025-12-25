rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
if rows <= 0 or columns <= 0 or rows==columns:
    print("Please enter positive integers for rows and columns, and ensure rows is not equal to columns.")
else:
    for i in range(rows):
        for j in range(columns):
            print("*", end=" ")
        print()