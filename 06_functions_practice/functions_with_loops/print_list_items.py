def list_items(list):
    for item in list:
         print(item, end=', ')
num_ele=int(input("Enter number of elements in the list: "))
items=[]
for i in range(num_ele):
    ele=input(f"Enter element {i+1}: ")
    items.append(ele)
print(f"The items in the list are: ", end='')
list_items(items)