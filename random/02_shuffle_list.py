import random
num_of_elements=int(input("Enter the number of elements in the list: "))
elements_list=[]
for i in range(num_of_elements):
    element=input("Enter element {}: ".format(i+1))
    elements_list.append(element)
print(f"Original List: {elements_list}")
random.shuffle(elements_list)
print(f"List after first shuffle: {elements_list}")
random.shuffle(elements_list)
print(f"List after second shuffle: {elements_list}")