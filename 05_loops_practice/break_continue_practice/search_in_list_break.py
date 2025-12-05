num_ele=int(input("Enter the number of elements in the list: "))
num_list=[]
for i in range(num_ele):    
    element=int(input(f"Enter element {i+1}: "))
    num_list.append(element)
search_num=int(input("Enter the number to search in the list: "))
found=False
for num in num_list:
    if num==search_num:
        found=True
        print(f"{search_num} is found in the list {num_list} at index {num_list.index(num)}.")
        break
if not found:
    print(f"{search_num} is not found in the list {num_list}.")