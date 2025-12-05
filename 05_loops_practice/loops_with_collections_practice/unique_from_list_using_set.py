num_ele=int(input("Enter the number of elements in the list: "))
num_list=[]
for i in range(num_ele):
    element=int(input(f"Enter element {i+1}: "))
    num_list.append(element)
unique_elements=set()
for num in num_list:
    unique_elements.add(num)
print(f"The unique elements in the list {num_list} are: {unique_elements} and it's length is {len(unique_elements)}.")