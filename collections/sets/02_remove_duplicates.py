num_ele=int(input("Enter number of elements you want to add in the list (with duplicates): "))
my_list=[float(input("Enter element {}: ".format(i+1))) for i in range(num_ele)]
print("Original List with duplicates: ", my_list)
unique_set=set(my_list)
print("List after removing duplicates: ", list(unique_set))
