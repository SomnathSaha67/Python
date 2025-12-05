num_ele=int(input("Enter the number of elements in the dictionary: "))
marks={}
for i in range(num_ele):
    subject=input(f"Enter subject {i+1}: ")
    marks=int(input(f"Enter marks for subject '{subject}': "))
    marks[subject]=marks
print("The items in the marks dictionary are:")
for subject, mark in marks.items():
    print(f"Subject: {subject}, Marks: {mark}")