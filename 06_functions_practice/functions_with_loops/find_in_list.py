def find_in_list(list,target):
    for index in range(len(list)):
        if list[index]==target:
            return index
    return -1
num_ele=int(input("Enter number of elements in the list: "))
elements=[]
for i in range(num_ele):
    ele=input(f"Enter element {i+1}: ")
    elements.append(ele)
target=input("Enter the element to find: ")
result=find_in_list(elements,target)
if result!=-1:
    print(f"Element '{target}' found at index: {result}")
else:
    print(f"Element '{target}' not found in the list.")