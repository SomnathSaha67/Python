num_ele=int(input("Enter number of elements you want to add in the tuple: "))
my_tuple=tuple(input("Enter element {}: ".format(i+1)) for i in range(num_ele))
print("Original Tuple: ", my_tuple)
add_ele=input("Enter an element to add to the tuple: ")
my_tuple+= (add_ele,)
print("Tuple after adding element: ", my_tuple)
print("Sorted Tuple: ", tuple(sorted(my_tuple)))
print("Tuple after removing an arbitrary element: ", my_tuple[:-1])
print("Final Tuple: ", my_tuple)
#tuple unpacking
a, b, *rest = my_tuple # Unpacking the first two elements and the rest, '*' is 'catch-all operator'
print("First Element: ", a)             
print("Second Element: ", b)
print("Rest of the Elements: ", rest)
