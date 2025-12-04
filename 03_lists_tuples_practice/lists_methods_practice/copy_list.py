list=[1,2,3,4,5,6,7,8,9,10]
new_list=list.copy()
print("Original list:", list)
print("Copied list:", new_list)
new_list.append(11)
print("After appending 11 to copied list:", new_list)
print("Original list remains unchanged:", list)