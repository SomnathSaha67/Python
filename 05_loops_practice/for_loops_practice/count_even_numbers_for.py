num_ele=int(input("Enter the number of elements in the list: "))
num_list=[]
for i in range(num_ele):
    element=int(input(f"Enter element {i+1}: "))
    num_list.append(element) 
count=0
for num in num_list:
    if num%2==0:
        count+=1
print(f"The number of even numbers in the list {num_list} is {count}.")