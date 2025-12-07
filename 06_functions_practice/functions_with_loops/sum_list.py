def sum_list(list):
    sum=0
    for number in list:
        sum+=number
    return sum
num_ele=int(input("Enter number of elements in the list: "))
numbers=[]
for i in range(num_ele):
    ele=float(input(f"Enter number {i+1}: "))
    numbers.append(ele)
print(f"The sum of the list elements is: {sum_list(numbers)}")