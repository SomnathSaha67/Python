num_ele=int(input("Enter the number of elements in the list: "))
num_list=[]
sum=0
for i in range(num_ele):
    element=int(input(f"Enter element {i+1}: "))
    num_list.append(element) 
for num in num_list:
    sum+=num
print(f"The sum of all elements in the list {num_list} is {sum}.")