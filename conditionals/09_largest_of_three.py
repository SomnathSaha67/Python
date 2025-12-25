num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))
largest_number=num1 if num2<num1>num3 else num2 if num1<num2>num3 else num3 if num1<num3>num2 else "All numbers are equal"
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}.")