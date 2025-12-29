#Create 2D list (matrix), access elements, and modify an element and display the final 2D list
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        ele = float(input("Enter element at position ({}, {}): ".format(i+1, j+1)))
        row.append(ele)
    matrix.append(row)
print("Original 2D List (Matrix): ")
for row in matrix:
    print(row)
# Modify an element
mod_row = int(input("Enter the row number of the element to modify (1-{}): ".format(rows))) - 1
mod_col = int(input("Enter the column number of the element to modify (1-{}): ".format(cols))) - 1
new_value = float(input("Enter the new value: "))
matrix[mod_row][mod_col] = new_value
print("2D List (Matrix) after modification: ")
for row in matrix:
    print(row)