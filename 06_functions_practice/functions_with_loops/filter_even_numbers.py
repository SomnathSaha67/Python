def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
num_ele = int(input("Enter number of elements in the list: "))
numbers = []
for i in range(num_ele):                        
    ele = int(input(f"Enter element {i+1}: "))
    numbers.append(ele)
print(f"The even numbers in the list are: {filter_even_numbers(numbers)}")