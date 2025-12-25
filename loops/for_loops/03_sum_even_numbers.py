starting_number=int(input("Enter the starting number: "))
ending_number=int(input("Enter the ending number: "))
sum=0
for num in range(starting_number, ending_number + 1):
    if num % 2 == 0:
        sum += num
print(f"The sum of even numbers from {starting_number} to {ending_number} is: {sum}")