number=int(input("Enter a non-negative integer to compute its factorial: "))
while number < 0:
    print("Factorial is not defined for negative numbers. Please enter a non-negative integer.")
    number=int(input("Enter a non-negative integer to compute its factorial: "))
factorial=1
current=number
while current > 1:
    factorial *= current
    current -= 1
print(f"The factorial of {number} is {factorial}.")