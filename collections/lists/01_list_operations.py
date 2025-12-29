num_ele=int(input("Enter number of elements you want to add in the list: "))
my_list=[]
for i in range(num_ele):
    ele=float(input("Enter element {}: ".format(i+1)))
    my_list.append(ele)
print("Original List: ", my_list)
add_ele=float(input("Enter an element to add to the list: "))
my_list.append(add_ele)
print("List after adding element: ", my_list)
print("Sorted List: ", sorted(my_list))
print("Reverse Sorted List: ", sorted(my_list, reverse=True))