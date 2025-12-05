num_ele=int(input("Enter the number of elements in the tuple: "))
tuple_elements=()
for i in range(num_ele):
    element=int(input(f"Enter element {i+1}: "))
    tuple_elements+=(element,) 
search_num=int(input("Enter the number to search in the tuple: "))
found=False
for index in range(len(tuple_elements)):
    if tuple_elements[index]==search_num:
        found=True
        print(f"{search_num} is found in the tuple {tuple_elements} at index {index}.")
        break
if not found:
    print(f"{search_num} is not found in the tuple {tuple_elements}.")