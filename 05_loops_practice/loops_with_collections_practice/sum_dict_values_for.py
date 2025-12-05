num_ele=int(input("Enter the number of elements in the dictionary: "))
marks={}
for i in range(num_ele):
    subject=input(f"Enter subject {i+1}: ")
    marks=int(input(f"Enter marks for subject '{subject}': "))
    data_dict[subject]=marks
sum_marks=0
for marks in marks.values():
    sum_marks+=marks
print(f"The sum of all values in the dictionary {marks} is {sum_marks}.")