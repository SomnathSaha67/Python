num_ele=int(input("Enter number of elements you want to add in the list: "))
my_list=[float(input("Enter element {}: ".format(i+1))) for i in range(num_ele)]
print("Original List: ", my_list)