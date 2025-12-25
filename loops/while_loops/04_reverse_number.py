number=input("Enter a positive integer to reverse: ")
while not number.isdigit() or int(number) < 0:
    print("Invalid input. Please enter a positive integer.")
    number=input("Enter a positive integer to reverse: ")
print("Reversed number is:", number[::-1])